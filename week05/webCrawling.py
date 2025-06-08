import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class WebCrawler:
    def __init__(self, base_url, max_pages=50):
        self.base_url = base_url
        self.visited = set()
        self.to_visit = [base_url]
        self.max_pages = max_pages

    def is_valid_url(self, url):
        parsed_base = urlparse(self.base_url)
        parsed_url = urlparse(url)
        return parsed_url.scheme in ["http", "https"] and parsed_base.netloc == parsed_url.netloc

    def crawl(self):
        print(f"Starting crawl at: {self.base_url}\n")
        count = 0

        while self.to_visit and count < self.max_pages:
            url = self.to_visit.pop(0)

            if url in self.visited:
                continue

            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Failed to access {url}: {e}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            self.visited.add(url)
            count += 1
            print(f"[{count}] Crawled: {url}")

            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if self.is_valid_url(full_url) and full_url not in self.visited:
                    self.to_visit.append(full_url)

            time.sleep(1)  # Be nice to servers

        print("\nCrawl complete.")

# Usage
if __name__ == "__main__":
    start_url = "https://example.com"  # Replace with the starting URL
    crawler = WebCrawler(start_url, max_pages=20)
    crawler.crawl()