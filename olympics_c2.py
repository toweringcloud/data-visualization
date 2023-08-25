import requests
import json
from bs4 import BeautifulSoup

def get_olympics_participations():
    # Wikipedia 페이지 URL (올림픽 참가국별 참가 횟수 페이지)
    url = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"

    # 페이지 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 참가 횟수 정보가 있는 테이블 선택
    participation_table = soup.find("table", class_="wikitable")

    # 국가명과 참가 횟수를 저장할 딕셔너리 초기화
    data = {}

    # 테이블의 각 행을 순회하며 데이터 추출
    for row in participation_table.find_all("tr")[1:]:
        columns = row.find_all("td")

        if len(columns) >= 3:
            country = columns[0].text.strip().encode('ascii', 'ignore').decode('utf-8').split('(')[0]
            participations = columns[2].text.strip().replace(',', '')
            data[country] = {
                "participations": int(participations)
            }

    return data

# 결과 출력 (예시)
participations = get_olympics_participations()
for key, data in participations.items():
    print(f"{key} : {data['participations']}")

# JSON 파일로 저장
with open("olympics_participations.json", "w", encoding='cp949') as outfile:
    json.dump(participations, outfile, indent=4)