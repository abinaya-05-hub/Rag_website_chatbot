from scraper import scrape_website
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import store_chunks


def index_website(url):

    pages = scrape_website(url)

    all_chunks = []
    all_embeddings = []

    for page in pages:

        chunks = chunk_text(page["content"])

        embeddings = create_embeddings(chunks)

        for chunk, embedding in zip(chunks, embeddings):

            all_chunks.append({
                "text": chunk,
                "url": page["url"]
            })

            all_embeddings.append(embedding)

    store_chunks(url,all_chunks, all_embeddings)

    return {
        "pages": len(pages),
        "chunks": len(all_chunks)
    }