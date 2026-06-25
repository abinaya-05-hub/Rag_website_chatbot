from fastapi import FastAPI
from scraper import scrape_website
from indexer import index_website
from rag import ask_question

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

    result = index_website(url)

    return {
        "message": "Website indexed successfully",
        **result
    }


@app.get("/ask")
def ask(
    url: str,
    question: str
):

    answer = ask_question(
        url,
        question
    )

    return {
        "answer": answer
    }