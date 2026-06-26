from fastapi import FastAPI
from scraper import scrape_website
from indexer import index_website
from rag import ask_question
from fastapi import HTTPException
import traceback
from vector_store import get_collection


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "RAG Website Chatbot Backend Running"
    }


@app.get("/scrape")
def scrape(url: str):

    pages = scrape_website(url)

    return {
        "pages_scraped": len(pages),
        "sample": pages[0][:1000] if pages else ""
    }


@app.post("/index")
def index(url: str):

    try:

        result = index_website(url)

        return {
            "message": "Website indexed successfully",
            **result
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/ask")
def ask(url: str, question: str):
    try:
        answer = ask_question(url, question)
        return {"answer": answer}
    except Exception as e:
        traceback.print_exc()   # <-- This prints the full error
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/debug")
def debug(url: str):

    collection = get_collection(url)

    return {
        "count": collection.count()
    }