from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os

CHROMA_DB_PATH = 'chroma_db'

PROMPT_TEMPLATE = """You are a friendly assistant for Lux Grown, a premium lab-grown diamond jewelry brand. Use only the context below to answer the question. If the answer is not in the context say: I do not have that information right now please contact us directly. Be warm and professional.

Context: {context}

Question: {question}

Answer:"""

def load_qa_chain():
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 4})
   llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.3, openai_api_key=os.environ.get('OPENAI_API_KEY'))
    prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=['context', 'question'])
    def format_docs(docs):
        return '\n\n'.join(doc.page_content for doc in docs)
    chain = ({'context': retriever | format_docs, 'question': RunnablePassthrough()} | prompt | llm | StrOutputParser())
    return chain

def ask_question(chain, question):
    answer = chain.invoke(question)
    return {'answer': answer, 'sources': []}
