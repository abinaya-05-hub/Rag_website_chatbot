from embeddings import create_embeddings
from retriever import retrieve_chunks
from llm import generate_answer


def ask_question(url, question):

    query_embedding = create_embeddings([question])[0]

    docs = retrieve_chunks(
        url,
        query_embedding
    )

    if len(docs) == 0:
        return "No relevant information found."

    context = ""

    for doc in docs:

        context += f"""
Source: {doc['source']}

Content:
{doc['text']}

----------------------------

"""

    return generate_answer(
        context,
        question
    )