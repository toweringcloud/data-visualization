import pandas as pd
import json
from geopy.geocoders import Nominatim

# Geopy로 위치 정보 가져오기
geolocator = Nominatim(user_agent="olympics_locations")

# 국가 목록 (예시, 실제 데이터를 얻으려면 올바른 국가 목록을 가져와야 합니다)
countries = ["United States", "Russia", "China", "Japan", "Germany", "United Kingdom", "France", "Italy", "Australia", "South Korea"]

# 각 국가별 위치 정보를 저장할 딕셔너리 초기화
country_locations = {}

# 각 국가별 위도와 경도를 가져와 딕셔너리에 저장
for country in countries:
    location = geolocator.geocode(country)
    if location:
        country_locations[country] = {"latitude": location.latitude, "longitude": location.longitude}

# Wikipedia 정보 가져오기 (예시)
country_participations = {
    "United States": {"participations": 23},
    "Russia": {"participations": 13},
    # ... (다른 국가 정보)
}

# JSON 데이터로 합치기
final_data = {}
for country in country_locations:
    if country in country_participations:
        final_data[country] = {
            "latitude": country_locations[country]["latitude"],
            "longitude": country_locations[country]["longitude"],
            "participations": country_participations[country]["participations"]
        }

# 얻은 데이터를 DataFrame으로 변환
data = {
    "Country": ["United States", "Russia", "China", "Japan", "Germany", "United Kingdom", "France", "Italy", "Austraila", "Korea"],
    "Latitude": [37.0902, 61.524, 35.8617, 35.682839, 51.1657, 51.509865, 48.8566, 41.8719, -24.7761086, 36.638392],
    "Longitude": [-95.7129, 105.318756, 104.1954, 139.759455, 10.4515, -0.118092, 2.3522, 12.5674, 134.755, 127.6961188],
    "Participations": [23, 13, 10, 22, 16, 27, 28, 27, 164, 96]
}
df = pd.DataFrame(data)

# DataFrame을 CSV 파일로 저장
df.to_csv("olympics_participations_data.csv", index=False)