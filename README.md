# 🎬 YouTube Summarizer (Ollama Edition) 🚀

Effortlessly generate concise, multilingual summaries of YouTube videos and playlists using Ollama LLMs, LangChain, and a sleek PyQt5 GUI or Gradio web interface.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Interface](https://img.shields.io/badge/Interface-PyQt5%20%26%20Gradio-purple.svg)](https://github.com/Anas-KhanWP/youtube-summarizer-ollama)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-blue.svg)](https://ollama.com/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-orange.svg)](https://www.langchain.com/)

---

## 📑 Table of Contents

- [🔥 First Impressions](#-first-impressions)
- [🚀 Project Purpose](#-project-purpose)
- [📦 Features & Screenshots](#-features--screenshots)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧑‍💻 Installation & Usage](#-installation--usage)
- [✅ Examples & Output](#-examples--output)
- [📂 Project Structure](#-project-structure)
- [👥 Contribution Guidelines](#-contribution-guidelines)
- [🧪 Tests](#-tests)
- [📄 License & Attribution](#-license--attribution)
- [🏷️ Badges](#-badges-optional-but-eye-catching)

---

## 🔥 First Impressions

**YouTube Summarizer (Ollama Edition)**  
*Summarize YouTube videos and playlists in seconds, powered by local LLMs and a beautiful interface.*

---

## 🚀 Project Purpose

**What It Does:**  
This tool fetches YouTube transcripts and generates structured, multilingual summaries using advanced local LLMs. Use it via a modern GUI or a web interface.

**Why It Matters:**  
Save time by instantly extracting key points from long videos or playlists. Perfect for students, researchers, content creators, and anyone who needs quick insights from video content.

---

## 📦 Features & Screenshots

- 🎥 **Automatic Transcript Extraction**  
  Fetches subtitles via `youtube_transcript_api`.

- 🤖 **Ollama‑Powered Summarization**  
  Uses LangChain and models like `llama3`, `mistral`, etc.

- 🌐 **Multilingual Output**  
  Translate summaries into English, German, and more.

- 🖥️ **Two Interfaces**  
  - 📟 GUI via **PyQt5**
  - 🌐 Web App via **Gradio**

- 🛠️ **Configurable via `config.yaml`**  
  Set your preferred model, language, chunk size, and summary type.

- 📊 **Export to Excel**  
  Save summaries in structured Excel files.

**Screenshots:**  
![GUI Example](docs/UI%20example.png)

---

## 🛠️ Tech Stack

- ![Python](https://img.shields.io/badge/python-3.11-blue)
- [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Gradio](https://www.gradio.app/)
- [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/)
- [deep-translator](https://github.com/nidhaloff/deep-translator)
- [pandas](https://pandas.pydata.org/)
- [tqdm](https://tqdm.github.io/)

---

## 🧑‍💻 Installation & Usage

### 1. Clone & Install

```sh
git clone https://github.com/Anas-KhanWP/youtube-summarizer.git
cd youtube-summarizer
pip install -r requirements.txt
```

### 2. Start Ollama

Make sure [Ollama](https://ollama.com/) is installed and running locally.

### 3. Run the GUI

```sh
python gui.py
```

### 4. Run the Web App

```sh
python main.py
```

---

## ✅ Examples & Output

**Sample Input:**  
Paste a YouTube video or playlist URL.

**Sample Output:**  
- Title: Introduction  
  Summary: Overview of the video content...

- Title: Key Point 1  
  Summary: Explanation of the first major topic...

**Use Cases:**  
- Quickly summarize educational playlists  
- Extract meeting highlights  
- Translate video summaries for multilingual teams

---

## 📂 Project Structure

```
.
├── api.py
├── gui.py
├── main.py
├── requirements.txt
├── README.md
├── docs/
│   └── UI example.png
├── Results/
│   └── [Excel summary files]
└── ...
```

---

## 👥 Contribution Guidelines

1. Fork the repo and create your branch (`git checkout -b feature/your-feature`)
2. Commit your changes (`git commit -am 'Add new feature'`)
3. Push to the branch (`git push origin feature/your-feature`)
4. Open a Pull Request

Please follow [PEP8](https://pep8.org/) style and include tests for new features.

---

## 🧪 Tests

To run tests (if available):

```sh
python -m unittest discover
```

Or run any test scripts provided in the repo.

---

## 📄 License & Attribution

This project is licensed under the [MIT License](LICENSE).

**Acknowledgements:**
- [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Deep Translator](https://github.com/nidhaloff/deep-translator)
- [Gradio](https://www.gradio.app/)
- [PyQt5](https://pypi.org/project/PyQt5/)

---

## 🏷️ Badges (Optional but Eye-Catching)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Issues](https://img.shields.io/github/issues/Anas-KhanWP/youtube-summarizer)](https://github.com/Anas-KhanWP/youtube-summarizer/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Anas-KhanWP/youtube-summarizer)](https://github.com/Anas-KhanWP/youtube-summarizer/commits/main)

---