from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

print("Loading Docs...")
loader = DirectoryLoader("./files")
docs = loader.load()

print("Splitting Docs...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs_chunks = text_splitter.split_documents(docs)

print("Loading Embeddings...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

print("Creating Vector Store...")
vectorstore = Chroma.from_documents(docs_chunks, embeddings)