# 🎬 YouTube Summarizer (Ollama Edition) 🚀

Generate clear, concise summaries of YouTube videos using Ollama’s powerful LLMs, LangChain, and a sleek Python interface.

> ✨ Supports both Command Line & GUI (PyQt5)

---

## ✨ Features

- 🎥 **Automatic Transcript Extraction**  
  Extract subtitles from YouTube videos via `youtube_transcript_api`.

- 🤖 **Ollama‑Powered Summarization**  
  Uses LangChain and models like `llama3`, `mistral`, etc. from Ollama for natural, structured summaries.

- 🧠 **Multilingual Translation Support**  
  Summaries available in English, German, and more using `deep-translator`.

- 🪄 **Text Preprocessing**  
  Cleans HTML, special characters, and applies intelligent text chunking with `RecursiveCharacterTextSplitter`.

- 🖥️ **Dual Interface**  
  Choose between a CLI experience or a sleek PyQt5 desktop GUI.

- 📁 **Export Support**  
  Save summaries as `.txt` or `.csv` for further use.

---

## ⚙️ Requirements

- **Python** 3.8+
- [Ollama](https://ollama.com/) (must be installed & running)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) or `youtube_transcript_api`
- `pip install -r requirements.txt`

---

## 📦 Dependencies

Key libraries used:

- `langchain`, `langchain_ollama`, `tiktoken`
- `youtube_transcript_api`
- `deep-translator`
- `gradio`, `PyQt5`, `tqdm`, `pandas`

Install all via:

```bash
pip install -r requirements.txt
````

---

## 🚀 Quick Start (CLI)

```bash
git clone https://github.com/yourusername/youtube-summarizer-ollama.git
cd youtube-summarizer-ollama
pip install -r requirements.txt

# Run CLI tool
python summarize.py --url "https://www.youtube.com/watch?v=..."
```

---

## 🖥️ Quick Start (GUI)

```bash
python gui_app.py
```

Features:

* Paste a YouTube URL
* Choose language, model, summary style
* Click 'Summarize' and view results in real-time
* Export summaries

---

## 🛠️ Configuration

Modify `config.yaml` to:

* Select default Ollama model (e.g. `llama3`, `mistral`)
* Set translation language
* Adjust chunk size, chain type, or prompt template

---

## 📂 Project Structure

```
youtube-summarizer-ollama/
├── summarize.py         # CLI entry point
├── gui_app.py           # PyQt5 GUI app
├── summarizer.py        # Core logic for transcript & summary
├── config.yaml          # App configuration
├── prompts/             # Custom prompt templates
├── requirements.txt     # Dependencies
└── README.md
```

---

## ▶️ Usage Options

### CLI

```bash
python summarize.py --url "https://youtube.com/..." --lang de --style podcast --model mistral
```

### GUI

* Select video link
* Choose summary style (`brief`, `detailed`, `podcast`)
* Choose output language
* Click `Summarize`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [Ollama](https://ollama.com/)
* [LangChain](https://www.langchain.com/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
* [Deep Translator](https://github.com/nidhaloff/deep-translator)

---

## 💡 Author

Made with ❤️ by [Anas Khan](https://github.com/Anas-KhanWP)

---

## 🔗 Related Projects

* [LangChain Docs](https://docs.langchain.com/)
* [Ollama CLI](https://ollama.com/library)

```

---

Let me know if you'd like:
- A **version with badges**
- A **light/dark screenshot section**
- **GIF demo** support
- Or I can **auto-generate this README and commit it to your repo** via PR format.
