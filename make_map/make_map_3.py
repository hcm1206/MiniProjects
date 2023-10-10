# 지오코더 API를 이용하여 액셀 파일에 저장된 모든 주소들을 좌표로 변환

import requests
import pandas as pd

# 지오코더 API URL
apiurl = "http://api.vworld.kr/req/address?"
# 지오코더 API 파라미터 설정
params = {
    "service": "address",
    "request": "getcoord",
    "crs": "epsg:4326",
    "format": "json",
    "type": "road",
    "key": "*검열됨*"
}

# 액셀 파일 로드
df = pd.read_excel('식신리스트.xlsx')
# 불러온 액셀 파일의 데이터 출력
print(df)

# 불러온 데이터의 각 행 별로 반복
for idx, row in df.iterrows():
    # 주소 정보 추출
    address = row['주소(도로명)']
    # API 매개변수의 address 부분을 현재 행의 주소로 설정
    params['address'] = address

    # 지오코더 API에 GET 요청으로 좌표 정보 요청
    response = requests.get(apiurl, params=params)

    # 요청 성공(코드 200) 시
    if response.status_code == 200:
        # 요청에 대한 반응을 json으로 저장
        json_data = response.json()

        # 경도 좌표 추출
        x = json_data['response']['result']['point']['x']
        # 위도 좌표 추출
        y = json_data['response']['result']['point']['y']
        # 위도와 경도 좌표 출력
        print(f"주소: {address}, 위도: {y}, 경도: {x}")