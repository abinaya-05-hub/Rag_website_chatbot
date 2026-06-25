from scraper import scrape_website
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import store_chunks


def index_website(url):

    pages = scrape_website(url)

    all_chunks = []

    for page in pages:

        chunks = chunk_text(page)

        all_chunks.extend(chunks)

    embeddings = create_embeddings(all_chunks)

    store_chunks(
        url,
        all_chunks,
        embeddings
    )

    return {
        "pages": len(pages),
        "chunks": len(all_chunks)
    }