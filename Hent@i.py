import json
from time import sleep
import requests

# To add more reddits, copy the template.py file, name it to what the subreddit is called and add a import function below with its name after
import waifusgonewild
import thick_hentai
import ecchi
import hentai

input("Press Enter to start>>")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}

while True:
    hentai.getData()
    waifusgonewild.getData()
    thick_hentai.getData()
    ecchi.getData()
    print("waiting 4 hours for next download...")
    sleep(14400)