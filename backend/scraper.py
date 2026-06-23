import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def scrape_website(url, max_pages=10):

    pages_content = []

    def crawl(current_url):

        if len(visited) >= max_pages:
            return

        if current_url in visited:
            return

        visited.add(current_url)

        try:
            response = requests.get(current_url, timeout=10)

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            pages_content.append(text)

            base_domain = urlparse(url).netloc

            for link in soup.find_all("a", href=True):

                next_url = urljoin(
                    current_url,
                    link["href"]
                )

                if urlparse(next_url).netloc == base_domain:
                    crawl(next_url)

        except Exception as e:
            print(e)

    crawl(url)

    return pages_content