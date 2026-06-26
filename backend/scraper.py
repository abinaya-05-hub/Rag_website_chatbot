import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def scrape_website(base_url):

    visited = set()
    pages = []

    try:

        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        visited.add(base_url)

        text = soup.get_text(separator=" ", strip=True)

        pages.append({
            "url": base_url,
            "content": text
        })

        links = []

        for link in soup.find_all("a", href=True):

            full_url = urljoin(base_url, link["href"])

            if urlparse(full_url).netloc == urlparse(base_url).netloc:

                if full_url not in visited:
                    links.append(full_url)

        # Limit crawling to first 10 internal pages
        for link in links[:10]:

            try:

                response = requests.get(link, timeout=10)

                soup = BeautifulSoup(response.text, "html.parser")

                text = soup.get_text(separator=" ", strip=True)

                pages.append({
                    "url": link,
                    "content": text
                })

                visited.add(link)

            except:
                pass

    except Exception as e:
        print(e)

    return pages