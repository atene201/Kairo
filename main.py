import os
import logging 
from typing import Tuple
import chromadb
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from ingest import setup_chroma_database, collection_name


load_dotenv()


# ---------------------------------------------------------------------
# RAG Chatbot Setup
# ---------------------------------------------------------------------
def setup_rag_chatbot() -> Tuple[ChatGoogleGenerativeAI, chromadb.ClientAPI, GoogleGenerativeAIEmbeddings]:
    """Initialize the RAG chatbot with Google Generative AI and ChromaDB Cloud.

    Loads environment variables, authenticates with Google API, and connects to ChromaDB Cloud.

    Returns:
        Tuple[ChatGoogleGenerativeAI, chromadb.ClientAPI, GoogleGenerativeAIEmbeddings]:
            - llm: Google Gemini LLM instance
            - client: ChromaDB Cloud client
            - embeddings: Google Generative AI embedding function
    """
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            api_key=os.environ["GOOGLE_API_KEY"]
            )

        client, embeddings = setup_chroma_database()

        return llm, client, embeddings

    except Exception as e:
        print(f"Error initializing RAG chatbot: {e}")
        raise


def main():
    print("-" * 60)
    print("RAG Chatbot - Ask questions about your documents!")
    print("-" * 60)
    print()

    try:
        llm, client, embeddings = setup_rag_chatbot()
        print("Chatbot Ready!")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    while True:
        user_input = input("\nYou: ").strip()

        # Exit condition
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the chatbot. Goodbye!")
            break

        try:
            vector_store = Chroma(
                collection_name=collection_name,
                embedding_function=embeddings,
                client=client
                )
            retriever = vector_store.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 3}
                )

            query = user_input

            relevant_docs = retriever.invoke(query)

            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            prompt = f"""You are a helpful AI assistant. Use the following context to help you answer the question.

            Context:
            {context}

            Question: {query}

            Answer:"""


            response = llm.invoke(prompt)
            print(f"\nAI: {response.content}")

        except Exception as e:
            print(f"An error occurred while processing your request: {e}")

if __name__ == "__main__":
    main()



