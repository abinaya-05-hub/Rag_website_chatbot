import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./chromadb_data"
)


def get_collection(url):

    collection_name = (
        url.replace("https://", "")
           .replace("http://", "")
           .replace("/", "_")
           .replace(".", "_")
    )

    collection_name = f"collection_{collection_name}"

    return client.get_or_create_collection(
        name=collection_name
    )


def store_chunks(url, chunks, embeddings):

    collection = get_collection(url)

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )