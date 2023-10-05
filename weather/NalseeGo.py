# 인자로 입력된 도시의 기온 출력 프로그램

import requests
import argparse

# 프로그램에 대한 설명 추가 및 parser 설정
parser = argparse.ArgumentParser(description="날씨고는 입력한 도시의 현재 기온을 알려주는 프로그램 입니다.")
# 프로그램 실행 시 인자 입력받음(city 인자 필수)
parser.add_argument('--city', required=True, help='현재 기온을 알고 싶은 도시명')
# 입력받은 인자를 변수로 저장
args = parser.parse_args()
# 인자 중 city 인자를 변수로 저장
city = args.city

# 위도 경도 정보 API URL 문자열 설정
url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = city
url_limit = "&limit=1"
url_appid = "&appid="
appid = "485eabe2dcd87ec439f2269693edc8ff"

# 위도 경도 정보 API URL 조합
url = url_front + url_q + q + url_limit + url_appid + appid

# API를 통해 위도 경도 정보 요청하여 응답받은 데이터 json화하여 저장
result = requests.get(url)
json_data = result.json()

# 데이터 중 위도(y)와 경도(x) 정보 추출하여 저장
x = json_data[0]['lon']
y = json_data[0]['lat']

# 날씨 정보 API URL 문자열 설정
url_front1 = "https://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="
lat = str(y)
url_lon = "&lon="
lon = str(x)
url_units = "&units=metric"

# 날씨 정보 API URL 문자열 설정
url1 = url_front1 + url_lat + lat + url_lon + lon + url_units + url_appid + appid

# API를 통해 날씨 정보 요청하여 응답받은 데이터 json화하여 저장
result1 = requests.get(url1)
json_data1 = result1.json()

# 데이터 중 기온 정보 추출하여 저장
temperature = json_data1['main']['temp']
# 인자로 입력된 도시의 기온 최종 출력
print(f"현재 {q} 기온은 섭씨 {temperature}도입니다.")