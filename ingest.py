# ============================================================
# ChromaDB Cloud Setup & Document Ingestion Module
# ------------------------------------------------------------
# This module sets up a connection to ChromaDB Cloud, initializes
# Google Generative AI embeddings, and ingests local text files
# into a Chroma collection for retrieval-augmented generation (RAG).
# ============================================================

import os
import logging
from typing import Tuple
import chromadb
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from dotenv import load_dotenv


load_dotenv()

# -------------------------------------------------------------
# Constants
# -------------------------------------------------------------
collection_name = "my-rag-collection"


# -------------------------------------------------------------
# Database setup
# -------------------------------------------------------------
def setup_chroma_database() -> Tuple[chromadb.ClientAPI, GoogleGenerativeAIEmbeddings]:
    """Set up and authenticate ChromaDB Cloud connection.

    Initializes the Google Generative AI embeddings model and connects to
    the ChromaDB Cloud service using credentials stored in environment variables.

    Returns:
        Tuple[chromadb.ClientAPI, GoogleGenerativeAIEmbeddings]:
            A tuple containing:
            - client: Authenticated ChromaDB Cloud client.
            - embeddings: GoogleGenerativeAIEmbeddings instance.
    """
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


# -------------------------------------------------------------
# Document Ingestion
# -------------------------------------------------------------
def ingest_documents() -> None:
    """Ingest local text documents into ChromaDB Cloud collection."""
    print("Connecting to ChromaDB Cloud...")

    
    try:
        client, embeddings = setup_chroma_database()
        print("Connected to ChromaDB Cloud successfully.")

    except Exception as e:
        print(f"Failed to connect to ChromaDB Cloud: {e}")
        return

    print("Setting up collection...")
    try:
        collection = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            client=client
        )
        print(f"Collection '{collection_name}' is ready.")

    except Exception as e:
        print(f"Failed to set up collection: {e}")
        return

    print("Loading documents from local machine...")
    try:
        loader = DirectoryLoader("./data/", glob="**/*.txt", loader_cls=TextLoader)
        documents = loader.load()

        if not documents:
            print("No documents found in the specified directory. Please add documents and try again.")
            return

        print(f"Loaded {len(documents)} documents.")
        collection.add_documents(documents)
        print(f"Successfully ingested {len(documents)} documents into collection '{collection_name}'.")
    except Exception as e:
        print(f"Error while ingesting documents: {e}")


if __name__ == "__main__":
    ingest_documents()

