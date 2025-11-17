# Kairo
# Kairo — Personal AI Assistant

Kairo is a personalized AI assistant that uses **Retrieval-Augmented Generation (RAG)** to tailor responses based on your own documents and daily needs. By combining Google Gemini models with ChromaDB, Kairo retrieves your uploaded information to generate more accurate, context‑aware answers.

---

## 🚀 Features

* Personalized responses using your own notes, PDFs, and documents
* Integration with **Google Gemini** via Google AI Studio
* Document storage and retrieval using **ChromaDB**
* Simple setup and easy prompting experience

---

## 📦 Requirements

You will need accounts and API keys for:

### **1. Google AI Studio**

Used for accessing **Google Gemini** models.
[https://aistudio.google.com/](https://aistudio.google.com/)

### **2. ChromaDB**

Used to store and retrieve your embedded documents.
[https://www.trychroma.com/](https://www.trychroma.com/)

---

## 🛠️ Setup Instructions

### **1. Acquire the Required API Keys**

Get your Google AI Studio and ChromaDB API keys from their respective dashboards.

---

### **2. Clone the GitHub Repository**

Using SSH or HTTPS, clone the project to your local machine:

```
git clone <your‑repo‑url>
```

---

### **3. Create a `.env` File**

Inside the project root directory, create a `.env` file and add the following:

```
GOOGLE_API_KEY=...
CHROMADB_API_KEY=...
TENANT_ID=...
DATABASE_ID=...
```

Replace each placeholder with your actual key values.

---

### **4. Add Your Personal Documents**

Place any PDFs or text files inside the `data/` folder.

These documents help Kairo give more personalized responses.
**Example:** You can upload class notes, resumes, project descriptions, or any information about yourself.

---

### **5. Run the Setup Script**

Open a terminal in the project directory and run:

```
python setup.py
```

This script processes the files in `data/` and uploads them to your ChromaDB database.

---

### **6. Start the Assistant**

Run Kairo with:

```
python main.py
```

You can now begin prompting your personal AI assistant.

---

## 🧩 Additional Notes

* Ensure your `.env` file is not committed to Git for security reasons.
* You can update the `data/` folder anytime and rerun `setup.py` to refresh the database.

---

## 🎉 You're Ready to Use Kairo!

Enjoy personalized, context‑aware AI responses built around your own life and documents.
