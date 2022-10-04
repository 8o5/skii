import requests
from bs4 import BeautifulSoup

from polyscraper.helpers import config, headers, link


def scrapeData(link):
    data = requests.get(
            url=link,
            headers=headers,
            timeout=5,
        )
    z = BeautifulSoup(data.content, "html.parser")
    img_location = z.findAll('img', class_="product-featured-media")
    title_location = z.findAll('h1', class_="product-single__title")
    product_image = f"https:{img_location[1]['src']}" # type: ignore
    product_title = title_location[0].text
    return (product_image, product_title)

scrape = scrapeData(link=config["url"][link])

def check(url, headers):

    data = requests.get(
        url,
        headers,
        timeout=5,
    )

    data.raise_for_status()

    return data
