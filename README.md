# polyscraper
basic monitor for https://polyphia.com

## config.toml formatting rules
(please read comments before opening issue)
### products
* `products = ["url_1", "url_2"]` urls must start with `https://www.polyphia.com/products/`
* __variants will not work__ if the product link ends in `?variant=123456789` you must remove everything _after_ the `?`
### settings
* `cooldown=number` cooldown is in seconds, __going below `60` when monitoring for long periods of time is not recommended__ to prevent getting temporarily banned from the website
* `webhooks=bool` replace bool with true or false depending on if you want webhooks to send
### discord
* `webhook="link"` replace link with your own [webhook link](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
* `my_id=numbers` replace numbers with your own [discord id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-#:~:text=Enabling%20Developer%20Mode%20%2D%20Mobile%20App,and%20turn%20on%20Developer%20Mode.)

## example config
```
products = [
    "https://www.polyphia.com/products/remember-that-you-will-die-genesis-variant-lp",
    "https://www.polyphia.com/products/remember-that-you-will-die-ego-death-variant-lp",
    "https://www.polyphia.com/products/remember-that-you-will-die-memento-mori-variant-lp",
    "https://www.polyphia.com/products/polyheadbl-ts"
] 

[settings]
cooldown=60 
webhooks=false

[discord]
webhook="https://discord.com/api/webhooks/example" 
my_id=123456789
```
