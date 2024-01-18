# 15tKD_8cQrQ0cUKW9sN1
# XRElLB0ynx
# https://openapi.naver.com/v1/papago/n2mt
import json
import urllib.request

import response

client_id = '15tKD_8cQrQ0cUKW9sN1'
client_secret = 'XRElLB0ynx'
encoding_text = urllib.parse.quote("집가고싶다")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response)
    print(response['message']['result']['translatedText'])
    # print(response['translatedText'])