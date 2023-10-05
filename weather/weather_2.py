# 도시의 위도 경도 좌표와 날씨 확인

import requests

# 위도 경도 정보 API URL 문자열 설정
url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = 'q='
q = "Seoul"
url_limit = "&limit=1"
url_appid = "&appid="
appid = "485eabe2dcd87ec439f2269693edc8ff"

# API URL 조합 및 출력
url = url_front + url_q + q + url_limit + url_appid + appid
print(url, "\n")

# API를 통해 받아온 데이터 저장 및 json화하여 출력
result = requests.get(url)
json_data = result.json()
print(json_data)

# 위도 경도 데이터를 추출하여 저장 및 출력
x, y = json_data[0]['lon'], json_data[0]['lat']
print(f"{q}의 위도(y), 경도(x) 좌표 : ({y}, {x})")

# 날씨 정보 API URL 문자열 설정
url_front1 = "https://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="
lat = str(y)
url_lon = "&lon="
lon = str(x)
url_units = "&units=metric"

# API URL 조합 및 출력
url1 = url_front1 + url_lat + lat + url_lon + lon + url_units + url_appid + appid
print(url1, "\n")

# API를 통해 받아온 데이터 저장 및 json화하여 출력
result1 = requests.get(url1)
json_data1 = result1.json()
print(json_data1, "\n")
# 기온 데이터를 추출하여 저장
temperature = json_data1['main']['temp']

# 도시의 기온 출력
print(f"현재 {q} 기온은 섭씨 {temperature}도 입니다.")
