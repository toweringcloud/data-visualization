import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_olympic_countries():
    url = 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='wikitable')

    rows = table.find_all('tr')
    data = []

    for row in rows[1:]:  # Skip the header row
        columns = row.find_all(['th', 'td'])
        year = int(columns[0].text.strip())
        countries = int(columns[2].text.strip().replace(',', ''))
        data.append({'Year': year, 'Countries': countries})

    return data

# 데이터 가져오기
data = get_olympic_countries()

# 데이터를 DataFrame으로 변환하여 CSV 파일로 저장
df = pd.DataFrame(data)
df.to_csv('olympic_countries.csv', index=False)