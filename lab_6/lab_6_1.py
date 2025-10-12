# accessing multiple sites, consecutively and parallel

import threading
from utils import measure_time
import requests  # !require installation!
from bs4 import BeautifulSoup  # !require installation!

urls = [
    "https://quotes.toscrape.com",
    "https://httpbin.org",
    "https://jsonplaceholder.typicode.com",
    "https://www.example.com",
    "https://www.data.gov",
    "https://openlibrary.org",
    "https://www.iana.org",
    "https://www.thecatapi.com",
    "https://dog.ceo/dog-api/",
    "https://pokeapi.co",
]


def page_title(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        webpage_title = soup.title

        if webpage_title:
            print(f"webpage title: {webpage_title.text}")
        else:
            print("No title found.")
    else:
        print("Failed to retrieve the webpage. Status Code:", response.status_code)


def process_websites_regular(urls):
    for url in urls:
        page_title(url)


def process_websites_parallel(urls, threads_count=4):
    for i in range(0, len(urls), threads_count):
        current_urls = urls[i : i + threads_count]

        threads = [
            threading.Thread(target=page_title, args=[url]) for url in current_urls
        ]

        for t in threads:
            t.start()
        for t in threads:
            t.join()


print("\n\n")
measure_time(process_websites_regular, [urls], "process_websites_regular()")
measure_time(process_websites_parallel, [urls, 10], "process_websites_parallel()")
