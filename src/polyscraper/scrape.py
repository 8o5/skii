import requests
from bs4 import BeautifulSoup

from .helpers import config, headers
from .webhook import dataError


def scrapeData(link):

    data = requests.get(
        url=link,
        headers=headers,
        timeout=5,
    )

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
            dataError(type="DATA", data=data)

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
<<<<<<< Updated upstream

        collection_location = x.find(
            "a", class_="btn btn--secondary btn--has-icon-before"
        )

        if collection_location != None:
            collection_url = collection_location["href"]  # type: ignore
        else:
            dataError(data=collection_location)
            exit()
=======
>>>>>>> Stashed changes

        product_image = f"https:{img_location[1]['src']}"
        product_title = title_location[0].text

        return (product_image, product_title, instock)


def scrapeCollections():
    
    try:
        data = requests.get(
            url="https://www.polyphia.com/",
            headers=headers,
            timeout=5,
        )
        
    except:
        dataError(data=data)  # type: ignore
        exit()

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
            dataError(type= "DATA",data="https://www.polyphia.com/")

        print(data.status_code)
        exit()

    elif data.status_code == 200:
        x = BeautifulSoup(data.content, "html.parser")

        collections_location = x.findAll(
            "div",
            class_="site-nav__dropdown critical-hidden site-nav__dropdown--left",
        )
        
        for colletion in collections_location:
            collection_link = collection['href']
            collections.append(collection_link)
        
        collections_location['href']

        print()
