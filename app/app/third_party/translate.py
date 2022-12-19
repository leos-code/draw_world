import requests


def translator(text: str):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to[0]":"en","api-version":"3.0","from":"zh-Hans","profanityAction":"NoAction","textType":"plain"}
    payload = [{"Text": text}]
    headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "aa8b3a9627msh956b27ea8c79dacp156c12jsn6547c1d4e83a",
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    rsp = response.json()
    #response format: [{"translations":[{"text":"Today is a good day","to":"en"}]}]
    target_text = rsp[0]["translations"][0]["text"]
    return target_text


if __name__ == "__main__":
    text = "美丽的女孩, PAI人物引擎"
    target = translator(text)
    print(target)