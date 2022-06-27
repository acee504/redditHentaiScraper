import json
import requests

subreddit = "thick_hentai"
url = f"https://www.reddit.com/r/{subreddit}.json"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
data = requests.get(url, headers=headers).json()

# uncomment this to print all data:
# print(json.dumps(data, indent=4))
def getData():
    for ch in data["data"]["children"]:
        pic_url = ch["data"].get("url_overridden_by_dest")
        if pic_url:
            file_name = pic_url.split("/")[-1]
            if not "." in file_name:
                continue
            with open(f'files/{subreddit}/{file_name}', "wb") as f_out:
                print("Downloading {}".format(pic_url))
                c = requests.get(pic_url, headers=headers).content
                f_out.write(c)