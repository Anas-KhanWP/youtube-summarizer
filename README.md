# 🎬 YouTube Summarizer (Ollama Edition) 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GUI](https://img.shields.io/badge/Interface-PyQt5%20%26%20Gradio-purple.svg)](https://github.com/Anas-KhanWP/youtube-summarizer-ollama)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-blue.svg)](https://ollama.com/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-orange.svg)](https://www.langchain.com/)

Effortlessly generate concise, multilingual summaries of YouTube videos using [Ollama](https://ollama.com)'s cutting-edge LLMs, LangChain, and a sleek PyQt5 GUI or Gradio interface.

---

## ✨ Features

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

---

## 📂 Project Structure

```

youtube-summarizer-ollama/
├── api.py              # Backend logic for summarizing & translation
├── gui.py              # PyQt5 GUI app
├── main.py             # Gradio web interface
├── requirements.txt    # Dependencies
└── README.md

````

---

## ⚙️ Requirements

- **Python** 3.8+ (3.11.5 Preferred)
- [Ollama](https://ollama.com/) (installed & running locally)
- Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🚀 Quick Start

### 💻 Clone & Setup

```bash
git clone https://github.com/Anas-KhanWP/youtube-summarizer.git
cd youtube-summarizer
pip install -r requirements.txt
```

---

## 🖥️ GUI Usage (PyQt5)

```bash
python gui.py
```

Features:

* Paste a YouTube Playlist URL
* Choose Save Path
* Generate + And Save Summary in Excel

---

## 🌐 Web Usage (Gradio)

```bash
python main.py
```

* Launches Gradio interface in browser
* Clean interface for pasting video links and selecting options

---

## 📦 Key Libraries

* `langchain`, `langchain_ollama`, `tiktoken`
* `youtube_transcript_api`, `deep-translator`
* `PyQt5`, `gradio`, `pandas`, `tqdm`

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
* [Gradio](https://www.gradio.app/)
* [PyQt5](https://pypi.org/project/PyQt5/)

---

## 👤 Author

Made with ❤️ by [Anas Khan](https://github.com/Anas-KhanWP)

---