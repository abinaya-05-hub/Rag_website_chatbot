from embeddings import create_embeddings
from vector_store import store_chunks

chunks = [
    "Artificial Intelligence",
    "Machine Learning"
]

vectors = create_embeddings(chunks)

store_chunks(chunks, vectors)

print("Stored Successfully")