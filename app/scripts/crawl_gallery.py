import requests

cookies = {
    '__Host-next-auth.csrf-token': '44569da035b7a54a4c9660dfb873edc9254e36a5e9c55b4ee6bd917641c68ebd%7C02cae7e5172b91824eb8fda8b2c8c2f82d3361122cb1b0c90f173bf280e28b0f',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fopenart.ai',
    '_ga': 'GA1.1.713279864.1668824474',
    '_hjSessionUser_3111505': 'eyJpZCI6IjMwOGYyODk4LWJmMjktNWRkNi1hNTU1LWZhMTUzZWNlZWQ4OSIsImNyZWF0ZWQiOjE2Njg4MjQ0NzYzMTgsImV4aXN0aW5nIjp0cnVlfQ==',
    'themeMode': 'light',
    'themeDirection': 'ltr',
    'themeColorPresets': 'default',
    'themeLayout': 'horizontal',
    'themeContrast': 'default',
    'themeStretch': 'false',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_3111505': 'eyJpZCI6ImU2YWE3YzZkLTU0YWItNDBkMi04OTM3LTZiOGQwZDJhZmQwZCIsImNyZWF0ZWQiOjE2NzA0MTkxMjM5MjksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga_QYRJB9TLG7': 'GS1.1.1670419121.5.1.1670419142.39.0.0',
    '__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._24S4bNkquMH1kcf.D4PxM39gNzlnrmjx5O-03mIwn7rrupLa3IllDRZq4uO-nrIo1G9QDkUFKZ7app0m-3NmAsfk6vqyDxRqf608IaFralaGi6RUZE0D4_KXtrHdFWIGX-wY_p4VbGhfKNobL5dDZ8PNWneP5CyDw7OY_WktNia_Iqg7ybOUfaz-sHsmGQA0QTcYOnKurde4s7O9q9itdH-ZM86T1FuWukPTLQ9FSl7WfV4rZ0NiaAZbH69hiVvZFMzfZjy__BaqiS8W5vgWy4pB9WD02pQWIxpl_wD17oszsnWQ82Nb78f32c6jvX2RnfMnkwA4eVwf2R8A8UG-18FPx7b6Q7Padgg60jDv.mFkRddjxTjLFmz2_BmIx3g',
}

headers = {
    'authority': 'openart.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': '__Host-next-auth.csrf-token=44569da035b7a54a4c9660dfb873edc9254e36a5e9c55b4ee6bd917641c68ebd%7C02cae7e5172b91824eb8fda8b2c8c2f82d3361122cb1b0c90f173bf280e28b0f; __Secure-next-auth.callback-url=https%3A%2F%2Fopenart.ai; _ga=GA1.1.713279864.1668824474; _hjSessionUser_3111505=eyJpZCI6IjMwOGYyODk4LWJmMjktNWRkNi1hNTU1LWZhMTUzZWNlZWQ4OSIsImNyZWF0ZWQiOjE2Njg4MjQ0NzYzMTgsImV4aXN0aW5nIjp0cnVlfQ==; themeMode=light; themeDirection=ltr; themeColorPresets=default; themeLayout=horizontal; themeContrast=default; themeStretch=false; _hjIncludedInSessionSample=0; _hjSession_3111505=eyJpZCI6ImU2YWE3YzZkLTU0YWItNDBkMi04OTM3LTZiOGQwZDJhZmQwZCIsImNyZWF0ZWQiOjE2NzA0MTkxMjM5MjksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _ga_QYRJB9TLG7=GS1.1.1670419121.5.1.1670419142.39.0.0; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._24S4bNkquMH1kcf.D4PxM39gNzlnrmjx5O-03mIwn7rrupLa3IllDRZq4uO-nrIo1G9QDkUFKZ7app0m-3NmAsfk6vqyDxRqf608IaFralaGi6RUZE0D4_KXtrHdFWIGX-wY_p4VbGhfKNobL5dDZ8PNWneP5CyDw7OY_WktNia_Iqg7ybOUfaz-sHsmGQA0QTcYOnKurde4s7O9q9itdH-ZM86T1FuWukPTLQ9FSl7WfV4rZ0NiaAZbH69hiVvZFMzfZjy__BaqiS8W5vgWy4pB9WD02pQWIxpl_wD17oszsnWQ82Nb78f32c6jvX2RnfMnkwA4eVwf2R8A8UG-18FPx7b6Q7Padgg60jDv.mFkRddjxTjLFmz2_BmIx3g',
    'referer': 'https://openart.ai/discovery?discoveryModel=md',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = {
    'source': 'md',
    'cursor': '60',
}

#export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
proxies = {"https":"http://127.0.0.1:7890"}

#response = requests.get('https://openart.ai/api/feed/discovery', params=params, cookies=cookies, headers=headers, proxies=proxies)
#response_json = response.json()
# print(response_json)

import json
response_json = json.loads(open("./openart.page1", "r").read())

#TODO 写入数据库
host = "82.156.114.98"
user = "root"
passwd = "aBkVALtH"
db="draw_world"
port=5432

import psycopg2
conn = psycopg2.connect(host=host, user=user, password=passwd, port=port, database=db)
cursor = conn.cursor()


extract_data = []
result = response_json
for item in result["items"]:
    img_url = item["image_url"]
    prompt = item["prompt"]
    size = "%s:%s" % (item["image_width"], item["image_height"])
    extract_data.append((img_url, prompt, size, 1, 1, "stable diffusion"))

sql = "insert into gallery (img_url, prompt, size, stat, is_show, model_name) values (%s, %s, %s, %s, %s, %s)"
affect = cursor.executemany(sql,extract_data)
print("affect:", affect)


cursor.close()
conn.commit()
conn.close()
