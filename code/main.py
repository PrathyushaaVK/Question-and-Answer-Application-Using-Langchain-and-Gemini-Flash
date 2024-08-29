import streamlit as st
from database import create_vectordb, load_vectordb
from retrieval import get_relevant_docs, get_chain
from ui import display_header, display_footer

# Streamlit UI
display_header()

# Create vector database only if it doesn't exist
create_vectordb()

# Load vector database
vectorDb = load_vectordb()

# User query input
query = st.text_input("Enter your question:")

if query:
    retriever, relevant_docs = get_relevant_docs(query, vectorDb)
    chain, context = get_chain(retriever, relevant_docs)
    response = chain.invoke({"input": query, "context": context})
    st.header("Answer:")
    st.write(response['answer'])

# Footer
display_footer()
