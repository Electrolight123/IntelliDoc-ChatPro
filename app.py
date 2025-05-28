import streamlit as st
import os
import dotenv
import uuid

# check if it's linux so it works on Streamlit Cloud
if os.name == 'posix':
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, AIMessage

from rag_methods import (
    load_doc_to_db, 
    load_url_to_db,
    stream_llm_response,
    stream_llm_rag_response,
)

dotenv.load_dotenv()

# --- Use Groq's model ---
MODELS = [
    "groq/gemma2-9b-it",
    "groq/llama-guard-4-12b",
    "groq/llama-3.3-70b-versatile",
    "groq/qwen-qwq-32b"
]

st.set_page_config(
    page_title="RAG LLM Assistant 🤖", 
    page_icon="🤖", 
    layout="centered", 
    initial_sidebar_state="expanded"
)


# --- Header ---
st.html("""<h2 style="text-align: center;">🤖 <B>RAG LLM Assistant: Empower Your AI with Context</B></h2>""")


# --- Initial Setup ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "rag_sources" not in st.session_state:
    st.session_state.rag_sources = []

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there! How can I assist you today?"}
]


# --- Side Bar LLM API Tokens ---
with st.sidebar:
    if "GROQ_API_KEY" not in os.environ:
        default_groq_api_key = os.getenv("GROQ_API_KEY") if os.getenv("GROQ_API_KEY") is not None else ""  # only for development environment, otherwise it should return None
        with st.popover("🔐 Groq"):
            groq_api_key = st.text_input(
                "Introduce your Groq API Key (https://platform.groq.com/)", 
                value=default_groq_api_key, 
                type="password",
                key="groq_api_key",
            )

    else:
        groq_api_key = None
        st.session_state.groq_api_key = os.getenv("GROQ_API_KEY")


# --- Main Content ---
# Checking if the user has introduced the Groq API Key, if not, a warning is displayed
missing_groq = (("GROQ_API_KEY" not in os.environ) and (not st.session_state.get("groq_api_key"))) 
if missing_groq:
    st.write("#")
    st.warning("⬅️ Please introduce your Groq API Key to continue...")

else:
    # Sidebar
    with st.sidebar:
        st.selectbox(
            "🤖 Select a Model", 
            options=MODELS,
            key="model",
        )

        cols0 = st.columns(2)
        with cols0[0]:
            is_vector_db_loaded = ("vector_db" in st.session_state and st.session_state.vector_db is not None)
            st.toggle(
                "Use RAG", 
                value=is_vector_db_loaded, 
                key="use_rag", 
                disabled=not is_vector_db_loaded,
            )

        with cols0[1]:
            st.button("Clear Chat", on_click=lambda: st.session_state.messages.clear(), type="primary")

        st.header("RAG Sources:")
            
        # File upload input for RAG with documents
        st.file_uploader(
            "📄 Upload a document", 
            type=["pdf", "txt", "docx", "md"],
            accept_multiple_files=True,
            on_change=load_doc_to_db,
            key="rag_docs",
        )

        # URL input for RAG with websites
        st.text_input(
            "🌐 Introduce a URL", 
            placeholder="https://example.com",
            on_change=load_url_to_db,
            key="rag_url",
        )

        with st.expander(f"📚 Documents in DB ({0 if not is_vector_db_loaded else len(st.session_state.rag_sources)})"):
            st.write([] if not is_vector_db_loaded else [source for source in st.session_state.rag_sources])

    
    # Main chat app
    model_provider = st.session_state.model.split("/")[0]
    if model_provider == "groq":
        llm_stream = ChatGroq(
            api_key=(groq_api_key or st.session_state.get("groq_api_key")),
            model_name=st.session_state.model.split("/")[-1],
            temperature=0.3,
            streaming=True,
        )
    # ... existing conditions for other providers if needed ...
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            messages = [HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"]) for m in st.session_state.messages]

            if not st.session_state.use_rag:
                st.write_stream(stream_llm_response(llm_stream, messages))
            else:
                st.write_stream(stream_llm_rag_response(llm_stream, messages))

            
    
