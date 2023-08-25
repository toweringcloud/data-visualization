import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_olympics_countries():
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
        #ValueError: invalid literal for int() with base 10: 'Team (IOC code)'
        data.append({'Year': year, 'Countries': countries})

    return data

# 데이터 가져오기
countries = get_olympics_countries()

# 데이터를 DataFrame으로 변환하여 CSV 파일로 저장
df = pd.DataFrame(countries)
df.to_csv('olympics_countries.csv', index=False)