from gc import collect
from os import link
import requests
from bs4 import BeautifulSoup

from polyscraper.helpers import config, headers
from polyscraper.webhook import dataError


def scrapeData(link):

    data = requests.get(
        url=link,
        headers=headers,
        timeout=5,
    )

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
            dataError(data)

        print(data.status_code)
        exit()

    elif data.status_code == 200:

        x = BeautifulSoup(data.content, "html.parser")

        img_location = x.findAll("img", class_="product-featured-media")

        title_location = x.findAll("h1", class_="product-single__title")

        status_location = x.find(attrs={"aria-label": "Sold out"})

        if status_location is None:
            instock = True
        else:
            instock = False
            
        collection_location = x.find("a", class_="btn btn--secondary btn--has-icon-before")
        
        if collection_location != None:
            collection_url = collection_location["href"]
        else:
            dataError(data)
            exit()

        product_image = f"https:{img_location[1]['src']}"
        product_title = title_location[0].text

        return (product_image, product_title, instock, collection_url)


def scrapeCollection(collection):
    try:
        data = requests.get(
            url=f"https://www.polyphia.com/collections/{collection}",
            headers=headers,
            timeout=5,
        )
    except:
        dataError(data=data) # type: ignore
        exit()

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
            dataError(data)

        print(data.status_code)
        exit()

    elif data.status_code == 200:
        x = BeautifulSoup(data.content, "html.parser")

        link_location = x.findAll(
            "a",
            class_="grid-view-item__link grid-view-item__image-container full-width-link",
        )

        print(link_location)
