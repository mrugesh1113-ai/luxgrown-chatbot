from langchain_community.embeddings import SentenceTransformerEmbeddings 
from langchain_community.vectorstores import Chroma 
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import PromptTemplate 
from langchain_core.runnables import RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser 
CHROMA_DB_PATH = 'chroma_db' 
 
def load_qa_chain(): 
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2') 
    vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings) 
    retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 4}) 
    llm = OllamaLLM(model='llama3.2', temperature=0.3) 
    prompt = PromptTemplate(template='You are a Lux Grown assistant. Use context to answer. Context: {context} Question: {question} Answer:', input_variables=['context', 'question']) 
    def format_docs(docs): 
        return ' '.join(doc.page_content for doc in docs) 
    chain = ({'context': retriever | format_docs, 'question': RunnablePassthrough()} | prompt | llm | StrOutputParser()) 
    return chain 
 
def ask_question(chain, question): 
    answer = chain.invoke(question) 
    return {'answer': answer, 'sources': []} 
