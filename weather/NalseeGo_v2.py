# 중복되는 이름의 도시들을 구분할 수 있도록 기능을 추가한 기온 출력 프로그램

import requests
import argparse

# 프로그램 설명 작성 및 parser 설정
parser = argparse.ArgumentParser(description="날씨고는 입력한 도시의 현재 기온을 알려주는 프로그램입니다.")
# 도시 이름을 city 인자로 받음
parser.add_argument('--city', required=True, help="현재 기온을 알고 싶은 도시명")
# 출력할 중복되는 이름의 도시 개수를 num 인자로 받음(생략 가능하며 기본값은 1)
parser.add_argument('--num', required=False, default=1, help="조회 결과 수")
# 입력받은 인자들을 변수로 저장
args = parser.parse_args()
# 인자 중 city 인자 저장
city = args.city
# 인자 중 num 인자 저장
num = args.num

# 위도 경도 API URL 문자열 설정
url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = city
url_limit = "&limit=" + str(num)
url_appid = "&appid="
appid = "485eabe2dcd87ec439f2269693edc8ff"

# 위도 경도 API URL 조합
url = url_front + url_q + q + url_limit + url_appid + appid

# API를 통해 응답받은 위도 경도 좌표를 json화하여 저장
result = requests.get(url)
json_data = result.json()

# 입력받은 도시가 여러 개 존재할 경우 그 개수를 표시
print(f"날씨고에게 {q}의 현재 기온을 물어본 결과({len(json_data)}건 입니다)")

# 날씨 API URL 문자열 설정
url_front1 = "http://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="
url_lon = "&lon="
url_units = "&units=metric"

# API로부터 응답받은 json 데이터(각 도시)들을 반복하여 실행
for i, data in enumerate(json_data, 1):
    # 해당 도시의 위도(y), 경도(x) 값 추출 및 저장
    x, y = data['lon'], data['lat']

    lat = str(y)
    lon = str(x)

    # 추출한 위도 경도를 토대로 날씨 API URL 조합
    url1 = url_front1 + url_lat + lat + url_lon + lon + url_units + url_appid + appid

    # API로부터 해당 도시의 날씨 데이터를 응답받아 json화하여 저장
    result1 = requests.get(url1)
    json_data1 = result1.json()

    # 해당 도시의 기온 정보 추출
    temperature = json_data1['main']['temp']
    # 해당 도시의 실제 이름 추출
    name = json_data1['name']
    # 해당 도시의 소속 국가 추출
    country = json_data1['sys']['country']
    # 현재 도시의 인덱스, 도시명, 소속 국가와 기온 출력
    print(f"{i}. 현재 {name} ({country}) 기온은 섭씨 {temperature}도입니다.")