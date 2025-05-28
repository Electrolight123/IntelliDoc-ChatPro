<p align="center">
  <img src="assets/banner.png" alt="IntelliDoc ChatPro Banner" width="80%" />
</p>

<h1 align="center">IntelliDoc ChatPro 🤖📄</h1>

<div align="center">

  [![Run on Localhost](https://img.shields.io/badge/Run-Localhost-1f8ef1?style=for-the-badge&logo=streamlit)](http://localhost:8501)
  [![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-fc4c02?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
  [![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-blueviolet?style=for-the-badge)](https://www.langchain.com/)
  [![HuggingFace](https://img.shields.io/badge/Embeddings-HuggingFace-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/)
  [![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCA0ODAgNDgwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zOTQuMiAxMTYuM0wzMzYgMTY4LjIgMzI4LjYgMTcyLjggMzI4LjYgNzMuNEMzMjguNiAzMi4yIDMwNS4zIDE2LjYgMjcyLjYgMzIuNkwxNDAuNCA5NS43QzEwOC4yIDExMC42IDEwNy4yIDE1My4xIDEzOS4xIDE2OHY2MS43TDIwMi4xIDIyOWMyLjkgMS41IDYuNSAyLjQgMTAuMyAyLjQgMy4yIDAgNi4yLS42IDguOS0xLjZsMTI0LjMtNDkuNkMzNjQuMSAyNzYuNCAzNjguNiAyMzEuMSAzOTQuMiAyMTIuOFYxMTYuM1oiIGZpbGw9IiNmYjMwNDEiLz48cGF0aCBkPSJNMjQwIDI2OC4zYy0zLjItMS40LTYuNi0yLjMtMTAuMi0yLjMtMy42IDAtNy4xLjgtMTAuMiAyLjNMMTA1LjIgMzE4LjZjLTIyLjkgOS4xLTIyLjUgNDIuNSAwIDUxLjdsMTMzLjkgNTMuYzE4LjUgNy4zIDM5LjIgNy4zIDU3LjcgMGwxMzMuOS01My4yYzIyLjYtOS4xIDIyLjktNDIuMyAwLTUxLjVsLTEzNC0uMXoiIGZpbGw9IiNmYjMwNDEiLz48L3N2Zz4=)](https://groq.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

> 🧠 **AI-powered document question answering with persistent chat history**, built using Groq LLMs, HuggingFace Embeddings, and LangChain RAG — deployed via Streamlit for an intuitive UI.


---

## 🚀 Features

- 🧠 Groq LLM integration (Gemma, LLaMA3, Qwen, LLaMA-Guard)
- 🔍 Retrieval-Augmented Generation (RAG) with PDF, DOCX, TXT, MD, URLs
- 💬 Persistent Chat History using `st.session_state`
- 🧠 HuggingFace embedding + ChromaDB for document vector storage
- 📄 Upload limit: 10 documents or URLs
- 🧹 Clear chat and toggle RAG
- ⚙️ Streamlit UI – minimal, interactive

---

## 📸 UI Preview

<p align="center">
  <img src="assets/ui_mockup.png" alt="UI Mockup" width="80%" />
</p>

---

## 🛠️ Installation

```bash
git clone https://github.com/Electrolight123/intellidoc-chatpro.git
cd intellidoc-chatpro
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables
Create a `.env` file in the root folder with:
```
GROQ_API_KEY="your_groq_api_key"
HUGGINGFACE_API_KEY="your_huggingface_api_key"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 Supported LLM Models

- groq/gemma2-9b-it
- groq/llama-guard-4-12b
- groq/llama-3.3-70b-versatile
- groq/qwen-qwq-32b

---

## 💾 Chat History

The app stores chat messages per session, enabling ongoing conversations without losing context.

---

## 📁 Project Structure

```bash
intellidoc-chatpro/
├── app.py
├── rag_methods.py
├── requirements.txt
├── .env
├── docs/
│   ├── test_rag.pdf
│   └── test_rag.docx
├── assets/
│   ├── banner.png
│   └── ui_mockup.png
├── README.md
```

---

## 🧪 Sample Docs for Testing

Sample files for testing the RAG engine are available in the [`docs/`](docs/) folder:
- `test_rag_sample.pdf`
- `test_rag_sample.docx`

---

## 📜 License

MIT License. See LICENSE for details.

---

## 🙋 Contribution & Contact

Pull requests welcome! For questions or feature requests, open an issue or contact me at [Abhishekbala089@gmail.com].

---

## ⭐ Show Your Support

If you find this helpful, please ⭐ star the repo and share it!
