from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from config import api_key

# Initialize language model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001", temperature=0.3, google_api_key=api_key)

def get_relevant_docs(query, vectorDb):
    retriever = vectorDb.as_retriever()
    return retriever, retriever.get_relevant_documents(query)

def get_chain(retriever, relevant_docs):
    context = " ".join([doc.page_content for doc in relevant_docs])

    prompt_template = """Using the context provided, extract the exact text from the 'response' that answers the question.
                     Do not modify the response, and if the answer is unclear or not directly found in the context, state 'I don't know.'
                     
                     QUESTION: {input}
                     
                     CONTEXT: {context}"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["input", "context"])

    combine_docs_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=combine_docs_chain)
    
    return chain, context
