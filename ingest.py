import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_FOLDER = 'docs'
CHROMA_DB_PATH = 'chroma_db'

def ingest_documents():
    print('Loading documents from the docs folder...')
    if not os.path.exists(DOCS_FOLDER):
        os.makedirs(DOCS_FOLDER)
        print('Created docs folder. Please add your PDF files there and run this again.')
        return
    pdf_files = [f for f in os.listdir(DOCS_FOLDER) if f.endswith('.pdf')]
    if not pdf_files:
        print('No PDF files found in the docs folder. Please add your Lux Grown PDFs and run again.')
        return
    print(f'Found {len(pdf_files)} PDF file(s): {pdf_files}')
    loader = DirectoryLoader(DOCS_FOLDER, glob='**/*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    print(f'Loaded {len(documents)} page(s) from your documents.')
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=['\n\n', '\n', '.', ' '])
    chunks = splitter.split_documents(documents)
    print(f'Split into {len(chunks)} chunks for embedding.')
    print('Creating embeddings (this may take a minute on first run)...')
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_DB_PATH)
    print(f'Done! {len(chunks)} chunks stored in ChromaDB.')
    print('You can now run the chatbot with: streamlit run app.py')

if __name__ == '__main__':
    ingest_documents()
