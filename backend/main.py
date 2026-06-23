@app.get("/scrape")
def scrape(url: str):

    pages = scrape_website(url)

    return {
        "pages_scraped": len(pages),
        "sample": pages[0][:1000] if pages else ""
    }