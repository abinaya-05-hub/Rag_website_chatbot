import chromadb
import uuid

client = chromadb.PersistentClient(path="./chromadb_data")


def get_collection(url):

    collection_name = (
        url.replace("https://", "")
           .replace("http://", "")
           .replace("/", "_")
           .replace(".", "_")
    )

    return client.get_or_create_collection(
        name=f"collection_{collection_name}"
    )


def store_chunks(url, chunks, embeddings):

    collection = get_collection(url)

    ids = [str(uuid.uuid4()) for _ in chunks]

    documents = []
    metadatas = []

    for chunk in chunks:
        documents.append(chunk["text"])
        metadatas.append({
            "source": chunk["url"]
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=[e.tolist() for e in embeddings],
        metadatas=metadatas
    )