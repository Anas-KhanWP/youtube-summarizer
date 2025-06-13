from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound
from deep_translator import GoogleTranslator
import re
from urllib.request import urlopen
import html
import gradio as gr
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
import tiktoken
from tqdm import tqdm
import pandas as pd
from pytube import Playlist

# Prompt templates
MAP_TEMPLATE_TXT = """Write a detail summary of this text section of a Drama in bullet points.
Make Sure its in netflix like plot. 
Use '-' for bullet points and answer only the bullet points.
Text:
{text}

SUMMARY:"""
    
COMBINE_TEMPLATE_TXT = """Combine these summaries of a Drama into a final summary in bullet points ONLY!
Make Sure its in netflix like plot. 
Strictly Follow this pattern: Write '- Title: (Title of Key Point): \nSummary: (Summary of the Key Point)' for bullet points and answer only the bullet points.
Text:
{text}

FINAL SUMMARY:"""

QUESTION_TEMPLATE_TXT = """Write a detailed summary (in bullet points, using "-" for bullets) of the following:
<text>
{text}
</text>

SUMMARY:"""

REFINE_TEMPLATE_TXT = """Your job is to produce a final summary in bullet points (using "-" for bullets).
You are provided an existing summary here:
<existing_summary>
{existing_answer}
</existing_summary>

You are provided new text.
<new_text>
{text}
</new_text>

Given the new text, refine the original summary.
If the context isn't useful, return the original summary. Answer your summary only, not other texts.
Final Summary:
"""

# Configuration settings
model = "llama3.2"
base_url = "http://localhost:11434"
chunk_size = 2000  # this is in tokens
overlap_size = 0  # this is in tokens
temperature = 0.5
mapreduce_num_predict = 512
map_num_predict = 512  # number of tokens to predict, Default: 128, -1 = infinite generation, -2 = fill context
combine_num_predict = 2048
refine_num_predict = 2048

global config
config = {
    "model": model,
    "base_url": base_url,
    "chunk_size": chunk_size,
    "overlap_size": overlap_size,
    "temperature": temperature,
    "mapreduce_num_predict": mapreduce_num_predict,
    "map_num_predict": map_num_predict,
    "combine_num_predict": combine_num_predict,
    "refine_num_predict": refine_num_predict
}

global text_to_summarize
text_to_summarize = ""

def get_video_urls_from_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        return list(playlist.video_urls)
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []

def extract_video_id(url):
    """Extract YouTube video ID from URL."""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_youtube_info(url: str):
    """Get video title and description."""
    video_id = extract_video_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")
        
    video_url = f"https://youtube.com/watch?v={video_id}"
    content = urlopen(video_url).read().decode('utf-8')
    
    title_match = re.search(r'"title":"([^"]+)"', content)
    title = html.unescape(title_match.group(1)) if title_match else "Unknown Title"
    
    desc_match = re.search(r'"description":{"simpleText":"([^"]+)"', content)
    description = html.unescape(desc_match.group(1)) if desc_match else "No description available"
    
    return title, description

def get_youtube_transcript(url):
    """
    Extract transcript from a YouTube video URL.
    
    Args:
        url (str): YouTube video URL
        
    Returns:
        str: Full transcript text
    """
    try:
        video_id = extract_video_id(url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")
            
        yt_ap = YouTubeTranscriptApi()
            
        transcript_list = yt_ap.list(video_id)
        print(transcript_list)
        
        # Pick the first available transcript (auto or manual)
        transcript = transcript_list.find_transcript(transcript_list._manually_created_transcripts.keys()
                                                     or transcript_list._generated_transcripts.keys())
        print(f"=========== Selected Transcript: {transcript} ===========")
        
        transcript_data = transcript.fetch()
        
        print(f"===================== Transcript Data =====================")
        # print(transcript_data)
        full_transcript = ' '.join(entry.text for entry in transcript_data)

        enc = tiktoken.encoding_for_model("gpt-4")
        count = len(enc.encode(full_transcript))
        
        return full_transcript, count
        
    except Exception as e:
        return f"Error: {str(e)}", 0
    
def get_text_splitter(chunk_size: int, overlap_size: int):
    """Get text splitter."""
    return RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, chunk_overlap=overlap_size)
    
def convert_text_to_split_docs(text, chunk_size, overlap_size):
    """Convert text to split documents."""
    docs = [Document(page_content=text)]
    text_splitter = get_text_splitter(chunk_size=chunk_size, overlap_size=overlap_size)
    split_docs = text_splitter.split_documents(docs)
    return split_docs

def get_larger_context_size(token_count):
    """Get larger context size."""
    num_ctxes = [1024 * i for i in range(1, 100)]
    num_ctx = next(ctx for ctx in num_ctxes if ctx > token_count)
    return num_ctx
    
def get_llm(model: str, base_url: str, temperature: float, num_ctx: int = 2048, num_predict: int = 256):
    """Get LLM."""
    llm = ChatOllama(
        model=model,
        base_url=base_url,
        temperature=temperature,
        num_ctx=num_ctx,
        num_predict=num_predict
    )
    return llm

def extract_structured_keypoints(text, video_title, video_url, summary):
    """
    Extract structured keypoints from a formatted summary text like:
    - Title: ...
    - Summary: ...
    """
    lines = text.strip().splitlines()
    row = {
        "Video URL": video_url,
        "Title": video_title,
        "Complete": summary.strip()
    }
    
    print("=====================================================")
    print(lines)
    print("=====================================================")

    keypoints = []
    title = summary_line = None

    for line in lines:
        line = line.strip()
        if "Title:" in line:
            title = line.split("Title:")[-1].strip()
        elif "Summary:" in line:
            summary_line = line.split("Summary:")[-1].strip()
            if title:
                keypoints.append((title, summary_line))
                title = summary_line = None  # Reset for next entry

    print(f"================================= Total Matches = {len(keypoints)} =================================")
    print(keypoints)

    for idx, (kp_title, kp_summary) in enumerate(keypoints, start=1):
        row[f"KeyPoint {idx} - Title"] = kp_title
        row[f"KeyPoint {idx} - Summary"] = kp_summary.replace("\n", " ")

    return row


# def extract_keypoints_to_excel(text, output_path='keypoints_summary_new.xlsx'):
#     """
#     Extracts key points from a structured summary text and writes them to an Excel file.

#     Args:
#         text (str): The input text containing structured key points.
#         output_path (str): Output Excel file path.
#     """
#     # Pattern to capture: Key Point (1): 'Title': Summary text
#     pattern = r"Key Point\s*\(?(\d+)\)?:\s*'([^']+)':\s*(.*?)\s*(?=(?:Key Point\s*\(?\d+\)?:)|\Z)"

#     matches = re.findall(pattern, text, flags=re.DOTALL)

#     # Prepare rows for DataFrame
#     data = []
#     for number, title, summary in matches:
#         key_point = f"{title.strip()}"
#         summary = summary.replace('\n', ' ').strip()
#         data.append((key_point, summary))

#     # Create DataFrame and export to Excel
#     df = pd.DataFrame(data, columns=["Key Point", "Summary"])
#     df.to_excel(output_path, index=False)
#     print(f"✅ Exported {len(df)} key points to '{output_path}'.")

def get_summary_map_reduce_langchain(text_to_summarize: str, map_prompt_txt: str, combine_prompt_text: str):
    """Get summary using map-reduce method with LangChain."""
    global config
    chunk_size = config["chunk_size"]
    overlap_size = config["overlap_size"]
    model = config["model"]
    base_url = config["base_url"]
    temperature = config["temperature"]
    mapreduce_num_predict = config["mapreduce_num_predict"]
    
    split_docs = convert_text_to_split_docs(text_to_summarize, chunk_size, overlap_size)
    
    tokens = (mapreduce_num_predict + chunk_size)
    num_ctx = get_larger_context_size(tokens)
    llm = get_llm(model, base_url, temperature, num_predict=mapreduce_num_predict, num_ctx=num_ctx)

    map_prompt = PromptTemplate(template=map_prompt_txt, input_variables=["text"])
    combine_prompt = PromptTemplate(template=combine_prompt_text, input_variables=["text"])
    
    chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=map_prompt, combine_prompt=combine_prompt, verbose=True)
    
    output = chain.invoke(split_docs)
    
    # extract_keypoints_to_excel(output['output_text'])  # Uncomment and pass actual text
    print("================== Output TEXT ==================")
    print(output["output_text"])
    
    return output['output_text']

def summarize_youtube_playlist_to_structured_excel(playlist_url, output_file='playlist_summary_structured.xlsx'):
    video_urls = get_video_urls_from_playlist(playlist_url)
    structured_data = []

    for video_url in tqdm(video_urls, desc="Summarizing"):
        try:
            title, description = get_youtube_info(video_url)
            transcript_text, token_count = get_youtube_transcript(video_url)
            
            if token_count == 0 or transcript_text.startswith("Error"):
                print(f"⚠️ Skipping '{title}' due to transcript issue.")
                continue
            
            summary = get_summary_map_reduce_langchain(
                transcript_text,
                MAP_TEMPLATE_TXT,
                COMBINE_TEMPLATE_TXT
            )

            structured_row = extract_structured_keypoints(
                summary,
                video_title=title,
                video_url=video_url,
                summary=summary
            )
            structured_data.append(structured_row)

        except Exception as e:
            print(f"❌ Error in Summary Func: {e}")

    df = pd.DataFrame(structured_data)
    df.index += 1
    df.index.name = "Index"
    df.to_excel(output_file)
    print(f"✅ Structured summary exported to {output_file}")

def export_playlist_summary_to_excel(summary_data, output_file='playlist_summary.xlsx'):
    df = pd.DataFrame(summary_data)
    df.to_excel(output_file, index=False)
    print(f"✅ Exported playlist summary to {output_file}")

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLb2aaNHUy_gGJruANTdvOM5HBVpvmXySY"
    all_summaries = summarize_youtube_playlist_to_structured_excel(playlist_url)
    export_playlist_summary_to_excel(all_summaries)
