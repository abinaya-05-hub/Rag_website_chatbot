import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text

    except Exception as e:
        return f"Error: {str(e)}"