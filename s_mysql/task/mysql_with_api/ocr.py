# https://ocr.space/OCRAPI
# K83789569288957
# 회원가입시 이메일이 온다, 이메일 인증을하면 또 이메일이 오는데 거기 비밀번호가 있다

# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests

def image_ocr(image_url):

    url = f'https://api.ocr.space/parse/imageurl?apikey=K83789569288957&url={image_url}&language=kor&isOverlayRequired=true'

    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    return result['ParsedResults'][0]['ParsedText']
    # print(type(result))
    # print(result['ParsedResults'][0]['ParsedText'])

