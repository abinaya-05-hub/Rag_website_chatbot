from fastapi import FastAPI
from scraper import scrape_website

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "RAG Website Chatbot Backend Running"
    }


@app.get("/scrape")
def scrape(url: str):

    content = scrape_website(url)

    return {
        "content": content[:1000]
    }