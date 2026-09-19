# GenAI RAG Project

A simple Retrieval-Augmented Generation (RAG) application built using Python, ChromaDB, Sentence Transformers, and Ollama.

## Project Overview

This project allows users to ask questions about company policy documents.

The system:
1. Reads the company document
2. Splits the document into chunks
3. Converts chunks into embeddings
4. Stores embeddings in ChromaDB
5. Retrieves the most relevant information
6. Sends the retrieved context to a local LLM
7. Generates an answer using Ollama

## Technologies Used

- Python
- Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2 1B
- Vector Embeddings
- RAG (Retrieval-Augmented Generation)

## RAG Pipeline

User Question  
↓  
Question Embedding  
↓  
ChromaDB Similarity Search  
↓  
Relevant Document  
↓  
Prompt + Context  
↓  
Llama 3.2  
↓  
Final Answer

## Example

Question:
How many vacation days do employees get?

Answer:
Employees get 18 days of annual leave.

## Project Structure

`text
gen-ai-rag-project/
│
├── documents/
│   └── company_policy.txt
│
├── .vscode/
│   └── settings.json
│
├── app.py
└── README.md