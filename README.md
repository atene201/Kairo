# Kairo — Personal AI Assistant

Kairo is a personalized AI assistant that uses Retrieval-Augmented Generation (RAG) to tailor responses based on your own documents and daily needs. By combining Google Gemini models with ChromaDB, Kairo retrieves your uploaded information to generate more accurate, context-aware answers.

## 🚀 Features

* Personalized responses using your own notes, PDFs, and documents
* Integration with Google Gemini via Google AI Studio
* Document storage and retrieval using ChromaDB
* Simple setup and easy prompting experience

## 📦 Requirements

You will need accounts and API keys for:

1. **Google AI Studio**  
   Used for accessing Google Gemini models. https://aistudio.google.com/

2. **ChromaDB**  
   Used to store and retrieve your embedded documents. https://www.trychroma.com/

## 💻 Installing Dependencies on Your Local Machine

Before running the assistant, install all Python requirements.

### 1. Create/Activate a Virtual Environment (recommended)

```bash
python -m venv venv
```

**Activate it:**

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 2. Install Project Requirements

The project includes a `requirements.txt` file with all necessary dependencies. Install them by running:

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- Google Generative AI SDK
- ChromaDB client
- Python-dotenv for environment management
- PyPDF2 or similar for document processing
- And all other project dependencies

**Tip:** If you need to update or regenerate the requirements file in the future, you can run:

```bash
pip freeze > requirements.txt
```

You are now ready to run the assistant locally.

## 🛠️ Setup Instructions

### 1. Acquire the Required API Keys

Get your Google AI Studio and ChromaDB API keys from their respective dashboards.

### 2. Clone the GitHub Repository

Use SSH or HTTPS to clone the repo:

```bash
git clone <your-repo-url>
```

Navigate to the project directory:

```bash
cd kairo
```

### 3. Create a `.env` File

In the project root directory, create a `.env` file containing:

```env
GOOGLE_API_KEY=...
CHROMADB_API_KEY=...
TENANT_ID=...
DATABASE_ID=...
```

Replace the placeholders with your actual values.

### 4. Add Your Personal Documents

Place any PDFs or text files inside the `data/` folder.

These documents help Kairo give personalized responses.

**Examples:**
* Class notes
* Resume or LinkedIn export
* Project documentation
* Personal goals or journal summaries

### 5. Run the Setup Script

Process and upload your documents to ChromaDB:

```bash
python setup.py
```

### 6. Start the Assistant

Launch Kairo:

```bash
python main.py
```

You can now begin prompting your own personalized AI assistant.

## 🧩 Additional Notes

* **Do not commit your `.env` file to Git.** Add it to your `.gitignore` file.
* You may add or remove documents anytime—just rerun `setup.py` to refresh the database.
* Ensure your virtual environment is activated before running any commands.

## 🎉 You're Ready to Use Kairo!

Enjoy personalized, context-aware AI responses tailored to your own documents, goals, and knowledge.
