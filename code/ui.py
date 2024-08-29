import streamlit as st

def display_header():
    st.set_page_config(page_title="EdTech Q&A", page_icon=":books:")
    st.image("../static/q&A.jpg", use_column_width=True)
    st.title("EdTech Q&A :books:")
    st.markdown("""
    Welcome to the **EdTech Q&A** app! Ask your questions about online educational courses, and we'll provide the best answers available.
    """)

def display_footer():
    st.markdown("""
    Made with :heart: using Streamlit and LangChain.
    """)
