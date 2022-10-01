import time

import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed


url = "https://www.polyphia.com/products/remember-that-you-will-die-genesis-variant-lp"

def notify():
    webhook = DiscordWebhook(
                        url="https://discord.com/api/webhooks/1025673303005855814/OZ64uC8kVtigwp6gH_OkeVt4syRp8VHX6Lk6qNPmZINO_QW42e-EZdVBGUMy6ugzsxCB")

    embed = DiscordEmbed(
                            title=f'🎉 ITEM INSTOCK', description='', color='161955')

    embed.set_author(name=f"Polyphia", url='https://www.polyphia.com/',
                    icon_url='https://cdn.shopify.com/s/files/1/0271/6018/2883/files/POLYPHIA_OW-3_180x.png?v=1657731615')  # set author

    embed.set_image(url='')  # set image

    embed.set_thumbnail(url='https://cdn.shopify.com/s/files/1/0271/6018/2883/products/WHITE_SILVERSMUSH_1024x1024@2x.png?v=1662044356')  # set thumbnail

    embed.set_footer(text='nic#0002',
                    icon_url='https://cdn.discordapp.com/avatars/249547320306171907/d0f228743a5d8164043d75834abb755c.png')  # set footer

    embed.set_timestamp()  # set timestamp (default is now)

    embed.add_embed_field(name='URL', value=f"{url}s", inline=False)

    webhook.add_embed(embed)
    webhook.execute()


def check(url, headers):

    data = requests.get(
        url,
        headers,
        timeout=5,
    )


    data.raise_for_status()

    if data.status_code != 200:
        print(
            f"ERROR {data.status_code}: UNABLE TO LOAD PAGE",
            end="\r",
        )

    elif data.status_code == 200:

        x = BeautifulSoup(data.content, "html.parser")

        try:
            status = x.find_all(attrs={"aria-label": "Sold out"})

            if len(status) == 0:
                raise TypeError

            time.ctime()
            print(
                f"[{time.ctime()}] -- OOS"
            )

        except:
            status = x.find_all(attrs={"aria-label": "Add to cart"})
            
            time.ctime()
            print(
                f"[{time.ctime()}] -- INSTOCK"
            )
            notify()


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

print(
    f"SCANNING {url}"
)

while True:
    check(
        url=url, 
        headers=headers
        )
    time.sleep(60)