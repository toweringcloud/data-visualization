import pandas as pd

# 얻은 데이터를 DataFrame으로 변환
data = {
    "Country": ["United States", "Russia", "China", "Japan", "Germany", "United Kingdom", "France", "Italy"],
    "Latitude": [37.0902, 61.524, 35.8617, 35.682839, 51.1657, 51.509865, 48.8566, 41.8719],
    "Longitude": [-95.7129, 105.318756, 104.1954, 139.759455, 10.4515, -0.118092, 2.3522, 12.5674],
    "Participations": [23, 13, 10, 22, 16, 27, 28, 27]
}

df = pd.DataFrame(data)

# DataFrame을 CSV 파일로 저장
df.to_csv("olympics_participation_data.csv", index=False)

