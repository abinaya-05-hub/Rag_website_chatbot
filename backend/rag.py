from embeddings import create_embeddings
from retriever import retrieve_chunks
from llm import generate_answer


def ask_question(url,question):

    query_embedding = create_embeddings([question])[0]

    docs = retrieve_chunks(
        url,
        query_embedding
        )

    context = "\n".join(docs)

    answer = generate_answer(
        context,
        question
    )

    return answer