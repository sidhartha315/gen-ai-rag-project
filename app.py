# STEP 1: Read document
file_path = "documents/company_policy.txt"
with open(file_path, "r") as file:
    document = file.read()
    
# STEP 2:#chunking
chunks = document.split("\n")
print("chunks:")
for chunk in chunks:
    print(chunk)
# STEP 3: creating embeddings
from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
print("\nEmbeddings model loaded successfully!")

#STEP 4 convert chunks into embeddings
embeddings = model.encode(chunks)
print("\nEmbeddings created successfully!")
print("Number of chunks:",len(embeddings))
print("vector size:", len(embeddings[0]))

# STEP 5: connect to chromaDB
import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection(
    name = "company_policy"
)

#STEP 5: store documents and embeddings
collection.add(
    ids = ["doc1","doc2","doc3"],
    documents = chunks,
    embeddings = embeddings.tolist()
)
print("\ndocuments successfully stored in ChromaDB!")

# STEP 6 & 7: Multiple Questions with RAG

from ollama import chat

while True:

    # Ask user for a question
    question = input("\nAsk your question (type 'exit' to stop): ")

    # Stop the program
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Convert question into embedding
    query_embeddings = model.encode([question])

    # Search ChromaDB
    results = collection.query(
        query_embeddings=query_embeddings.tolist(),
        n_results=1
    )

    # Get relevant document
    retrieved_document = results["documents"][0][0]

    print("\nRetrieved document:")
    print(retrieved_document)

    # Create prompt for LLM
    prompt = f"""
Answer the user's question using only the context below.

Context:
{retrieved_document}

User Question:
{question}

Answer:
"""

    # Send prompt to Llama
    response = chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Get final answer
    answer = response.message.content

    print("\nFinal Answer:")
    print(answer)