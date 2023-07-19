import requests

URL = "https://www.opentable.com/state-of-industry"

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

try: 
    page = requests.get(URL, allow_redirects=False, timeout=10, headers = headers)
except requests.exceptions.Timeout as err: 
    print(err)

print(page.text)
