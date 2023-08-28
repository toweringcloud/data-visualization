import json
import pandas as pd
import time
from geopy.geocoders import Nominatim

# Geopy로 위치 정보 가져오기
geolocator = Nominatim(user_agent="olympics_participations")

# Wikipedia 정보 가져오기 (JSON 파일을 DataFrame으로 읽기)
country_participations = pd.read_json("olympics_c_result.json")

# JSON 데이터로 합치기
final_data = {"Country": [], "Latitude": [], "Longitude": [], "Participations": []}
for key, val in country_participations.items():

    # 20번 이상 참여한 국가일 경우, 위도와 경도 값을 구하기
    play_count = int(val['participations'])

    if play_count >= 20:
        location = geolocator.geocode(key)
        time.sleep(3)

        if location:
            country_participations[key]['latitude'] = location.latitude
            country_participations[key]['longitude'] = location.longitude

            # 최종 데이터를 배열 형태로 저장
            final_data["Country"].append(key)
            final_data["Latitude"].append(float(location.latitude))
            final_data["Longitude"].append(float(location.longitude))
            final_data["Participations"].append(play_count)

# 최종 데이터를 DataFrame으로 변환
df = pd.DataFrame(final_data)

# DataFrame을 CSV 파일로 저장
df.to_csv("olympics_i_result.csv", index=False)