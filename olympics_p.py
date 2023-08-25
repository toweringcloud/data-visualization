import folium
import pandas as pd

# CSV 파일에서 데이터 불러오기
df = pd.read_csv("olympics_participations_data.csv")

# 중심 위치 설정 (지도의 초기 중심)
center_location = [30, 0]

# 지도 생성
map_olympics = folium.Map(location=center_location, zoom_start=2)

# 올림픽 참가국별 위치 정보와 참가 횟수를 지도에 표시
for index, row in df.iterrows():
    country = row["Country"]
    latitude = row["Latitude"]
    longitude = row["Longitude"]
    participations = row["Participations"]

    # 마커에 표시할 텍스트
    popup_text = f"Country: {country}<br>Participations: {participations}"

    # 마커 추가
    folium.Marker(location=[latitude, longitude], popup=popup_text).add_to(map_olympics)

# 지도를 HTML 파일로 저장하거나, Jupyter Notebook에서 바로 출력
map_olympics.save("olympics_participations_map.html")
map_olympics