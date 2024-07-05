from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents

extracted_data=load_pdf("data/")
text_splitter=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=80)
text_chunks=text_splitter.split_documents(extracted_data)

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

persist_directory='db'
vectordb=Chroma.from_documents(documents=text_chunks,embedding=embeddings,persist_directory=persist_directory)
vectordb.persist()