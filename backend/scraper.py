import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque


def scrape_website(start_url, max_pages=10):

    visited = set()
    queue = deque([start_url])
    pages = []

    domain = urlparse(start_url).netloc

    while queue and len(visited) < max_pages:

        url = queue.popleft()

        if url in visited:
            continue

        visited.add(url)

        try:
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove unnecessary tags
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)

            if text:
                pages.append({
                    "url": url,
                    "content": text
                })

            # Find all links
            for link in soup.find_all("a", href=True):

                absolute_url = urljoin(url, link["href"])

                parsed = urlparse(absolute_url)

                # Only crawl same website
                if parsed.netloc == domain:

                    clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path

                    if clean_url not in visited:
                        queue.append(clean_url)

        except Exception as e:
            print("Error:", e)

    return pages