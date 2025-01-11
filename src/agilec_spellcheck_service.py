import requests

def get_response(word):
    URL = "https://api.languagetoolplus.com/v2/check"

    payload = {
        "text": word,
        "language": "en-US"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(URL, data=payload, headers=headers)
    response.raise_for_status()  

    return response.json()

def parse(response):
    return not response.get("matches", [])

def spellcheck(word):
    response = get_response(word)
    return parse(response)
    