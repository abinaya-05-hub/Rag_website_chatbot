from vector_store import get_collection


def retrieve_chunks(url, query_embedding, top_k=3):

    collection = get_collection(url)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,

        include=[
            "documents",
            "metadatas"
        ]
    )

    print(results)

    retrieved_chunks = []

    documents = results.get("documents", [])
    metadatas = results.get("metadatas", [])

    if not documents:
        return []

    for doc, meta in zip(documents[0], metadatas[0]):

        retrieved_chunks.append({
            "text": doc,
            "source": meta["source"]
        })

    return retrieved_chunks