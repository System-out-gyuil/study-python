# https://ocr.space/OCRAPI
# K83789569288957
# 회원가입시 이메일이 온다, 이메일 인증을하면 또 이메일이 오는데 거기 비밀번호가 있다

# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=K83789569288957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'

response = requests.get(url)
response.raise_for_status()

result = response.json()
print(type(result))
print(result['ParsedResults'][0]['ParsedText'])

