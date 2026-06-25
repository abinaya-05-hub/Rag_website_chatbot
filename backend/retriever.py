from vector_store import get_collection


def retrieve_chunks(
    url,
    query_embedding,
    top_k=3
):

    collection = get_collection(url)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )

    return results["documents"][0]