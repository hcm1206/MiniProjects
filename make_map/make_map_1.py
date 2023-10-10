import folium

# 좌표 위치에 해당하는 지도 정보 저장
my_map = folium.Map(location = [37.592670, 127.016374], zoom_start=16)
# 지도 정보를 html 파일로 저장
my_map.save('my_map.html')