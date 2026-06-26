import hashlib

import chromadb
import uuid

client = chromadb.PersistentClient(path="./chromadb_data")


def get_collection(url):

    url_hash = hashlib.md5(url.encode()).hexdigest()

    collection_name = f"website_{url_hash}"

    return client.get_or_create_collection(
        name=collection_name
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