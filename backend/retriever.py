from vector_store import collection

def retrieve_chunks(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]