# 지오코더 API를 이용하여 주소에 대한 좌표 정보 출력
import requests

# 지오코더 API URL
apiurl = "http://api.vworld.kr/req/address?"
# 지오코더 API 파라미터 설정
params = {
    "service": "address",
    "request": "getcoord",
    "crs": "epsg:4326",
    "address": "서울특별시 성북구 동소문로 102",
    "format": "json",
    "type": "road",
    "key": "*검열됨*"
}

# 지오코더 API에 GET 요청으로 좌표 정보 요청
response = requests.get(apiurl, params=params)

# 요청 성공(코드 200)시
if response.status_code == 200:
    # 요청에 대한 반응을 json으로 저장
    json_data = response.json()
    # json 데이터 출력
    print(json_data)

    # 경도 좌표 추출
    x = json_data['response']['result']['point']['x']
    # 위도 좌표 추출
    y = json_data['response']['result']['point']['y']
    # 위도와 경도 좌표 출력
    print(f"위도: {y}, 경도:{x}")