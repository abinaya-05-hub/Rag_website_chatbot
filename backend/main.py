
from rag import ask_question


@app.get("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {
        "answer": answer
    }