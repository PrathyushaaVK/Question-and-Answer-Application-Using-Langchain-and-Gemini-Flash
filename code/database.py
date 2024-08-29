import os
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
import streamlit as st
from config import vectordb_file_path

# Initialize embeddings
instructor_embeddings = HuggingFaceInstructEmbeddings()

def create_vectordb():
    if not os.path.exists(vectordb_file_path):
        loader = CSVLoader(file_path='../data/codebasics_faqs.csv', source_column='prompt')
        docs = loader.load()
        vectorDb = FAISS.from_documents(documents=docs, embedding=instructor_embeddings)
        vectorDb.save_local(vectordb_file_path)
        st.write("FAISS index created and saved locally.")
    else:
        st.write("FAISS index already exists. Skipping creation.")

def load_vectordb():
    return FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
