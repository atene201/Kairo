import os
import logging
from typing import Tuple
import chromadb
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv


load_dotenv()

collection_name = "my-rag-collection"

def setup_database() -> Tuple[chromadb.ClientAPI, GoogleGenerativeAIEmbeddings]:
    try: 
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=os.environ["GOOGLE_API_KEY"]
            )
        client = chromadb.CloudClient(
            api_key=os.environ["CHROMADB_API_KEY"],
            tenant=os.environ["TENANT_ID"],
            database=os.environ["DATABASE_ID"]
            )
        return client, embeddings
        
    except Exception as e:
        print(f"Failed to initialize ChromaDB Cloud Client: {e}")
        raise


def retrieving_documents() -> None:
    try:
        client, embeddings = setup_database()
        print("Connected to ChromaDB Cloud successfully.")

    except Exception as e:
        print(f"Failed to connect to ChromaDB Cloud: {e}")
        return

    # Set up Chroma collection
    try:
        collection = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            client=client
        )
    except Exception as e:
        print(f"Failed to set up collection: {e}")
        return

    try:
        loader = DirectoryLoader("./data/", glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            print("No documents found in the specified directory. Please add documents and try again.")
            return

        collection.add_documents(documents)
        print(f"Successfully retrieved {len(documents)} documents into '{collection_name}'.")
    except Exception as e:
        print(f"Error while retrieving documents: {e}")


if __name__ == "__main__":
    retrieving_documents()

