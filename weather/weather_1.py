# 도시의 위도 경도 좌표 확인

import requests

# openweathermap의 API URL 문자열 설정
url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = "Seoul"
url_limit = "&limit=1"
url_appid = "&appid="
appid = "485eabe2dcd87ec439f2269693edc8ff" # API KEY 입력

# 최종 API URL 조합 및 출력
url = url_front + url_q + q + url_limit + url_appid + appid
print(url, "\n")

# API requests로 데이터 로드
result = requests.get(url)
# 로드된 데이터 json 형식으로 저장
json_data = result.json()
# json 데이터 출력
print(json_data, "\n")

# json 데이터에서 위도 경도 데이터 추출 및 출력
x, y = json_data[0]['lon'], json_data[0]['lat']
print(f"{q}의 위도(y), 경도(x) 좌표 : ({y}, {x})")