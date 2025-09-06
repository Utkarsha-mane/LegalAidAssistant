import streamlit as st
import fitz  # PyMuPDF for PDFs
from docx import Document
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# -------- CONFIG --------
USERS = {
    "official": "secure123",
    "judge": "court2025",
    "clerk": "records"
}

# -------- Helper functions --------
def read_file(file):
    """Read text from txt, pdf, docx"""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")
    elif file.name.endswith(".pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text("text") for page in pdf])
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(s) for s in summary])

def answer_question(question, text):
    docs = [text]
    vectorizer = TfidfVectorizer().fit(docs + [question])
    text_vec = vectorizer.transform(docs)
    q_vec = vectorizer.transform([question])
    scores = np.dot(text_vec, q_vec.T).toarray().ravel()
    return "Relevant part: " + text[:500]  # crude but works for demo

# -------- Streamlit UI --------
st.set_page_config(page_title="Legal Case Assistant", layout="wide")
st.title("⚖️ Legal Case Assistant (Offline Prototype)")

# --- Login system ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔒 Login Required")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful ✅")
        else:
            st.error("Invalid credentials ❌")
    st.stop()

# --- After login ---
st.success("Welcome, authorized official ✅")

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload a case document", type=["txt", "pdf", "docx"])

if uploaded_file:
    text = read_file(uploaded_file)

    st.subheader("📄 Extracted Text (first 1000 characters)")
    st.write(text[:1000] + "...")

    # --- Summarization ---
    if st.button("📝 Summarize Document"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
        st.subheader("📌 Case Summary")
        st.write(summary)

    # --- Question Answering ---
    st.subheader("💬 Ask Questions about the case")
    question = st.text_input("Enter your question")
    if question:
        with st.spinner("Finding answer..."):
            answer = answer_question(question, text)
        st.write("**Answer:**", answer)
