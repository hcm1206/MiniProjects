# 액셀 파일의 주소에 해당하는 좌표를 지도에 표시

import folium
import requests
import pandas as pd

# 좌표 위치에 해당하는 지도 정보 저장
my_map = folium.Map(location=[37.592670, 127.016374], zoom_start=16)

# 지오코드 API URL
apiurl = "http://api.vworld.kr/req/address?"
# 지오코드 API 파라미터 설정
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

# 불러온 액셀 데이터의 각 행별로 반복
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

        # 추출한 위도 경도 위치를 지도에서 마커로 표시 
        folium.Marker([y, x], popup=row['이름']).add_to(my_map)

# 지도 정보를 html 파일로 저장
my_map.save('my_map.html')