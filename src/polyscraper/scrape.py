<<<<<<< Updated upstream
=======
import sys
from typing import List, Tuple

>>>>>>> Stashed changes
import requests
from bs4 import BeautifulSoup

from .helpers import config, headers
from .webhook import dataError


def scrapeProducts():

    data = requests.get(
        url="https://www.polyphia.com/collections/all",
        headers=headers,
        timeout=5,
    )

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
            dataError(type="DATA", data=data.url)

        sys.exit(data.status_code)

    elif data.status_code == 200:

        all_products = []

        x = BeautifulSoup(data.content, "html.parser")

        all_products = x.findAll("div", class_="grid-view-item product-card")
        all_products.extend(x.findAll("div", class_="grid-view-item grid-view-item--sold-out product-card"))

        products = {}
        for product_data in all_products:
            data = {}

            img_location = product_data.contents[5].contents[1].contents[1].contents[1].attrs["data-src"]
            img_url = img_location.replace("{width}", "540")

<<<<<<< Updated upstream
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
=======
            if product_data.contents[11].contents[7].contents[3].contents[1].contents[0] == "Sold out":
                instock = "OOS"
            else:
                instock = "IN STOCK"
>>>>>>> Stashed changes

            data.update(
                {
                    "name": product_data.contents[9].contents[0],
                    "url": product_data.contents[1].attrs["href"],
                    "img": f"https://{img_url[2:]}",
                    "instock": instock,
                    "price": product_data.contents[11].contents[1].contents[3].contents[1].contents[0][:-1]
                }
            )
            my_product = Product(data)
            products.update({f"https://www.polyphia.com{product_data.contents[1].attrs['href']}": my_product})

        return products


<<<<<<< Updated upstream
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
=======
def scrapeCollections(list_collections, all_list_collections):

    data = requests.get(
        url="https://www.polyphia.com/collections/",
        headers=headers,
        timeout=5,
    )
>>>>>>> Stashed changes

    data.raise_for_status()

    if data.status_code != 200:  # site response error handling

        if config["settings"]["webhooks"] == True:
<<<<<<< Updated upstream
            dataError(type= "DATA",data="https://www.polyphia.com/")

        print(data.status_code)
        exit()
=======
            dataError(type="DATA", data=data.url)

        sys.exit(data.status_code)
>>>>>>> Stashed changes

    elif data.status_code == 200:
        x = BeautifulSoup(data.content, "html.parser")

<<<<<<< Updated upstream
        collections_location = x.findAll(
            "div",
            class_="site-nav__dropdown critical-hidden site-nav__dropdown--left",
        )
        
        for colletion in collections_location:
            collection_link = collection['href']
            collections.append(collection_link)
        
        collections_location['href']

        print()
=======
        all_collections = x.findAll("div", class_="collection-grid-item__title h3")

        filtered_collections = x.findAll("a", class_="collection-grid-item__link")

        for collection in all_collections:

            all_list_collections.append(str.strip(collection.text))

        for collection in filtered_collections:

            if collection["href"] != "#":
                list_collections.append(collection["href"].split("/")[2])

        return (list(list_collections), list(all_list_collections))
>>>>>>> Stashed changes
