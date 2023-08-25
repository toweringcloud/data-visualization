import matplotlib.pyplot as plt
import pandas as pd

# 연도별 올림픽 참가국 수 데이터 (출처: Wikipedia)
data = {
    "Year": [1896, 1900, 1904, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020],
    "Countries": [12, 24, 14, 22, 28, 29, 44, 46, 37, 49, 59, 69, 72, 83, 93, 112, 121, 92, 80, 140, 160, 169, 197, 200, 201, 201, 204, 207, 206, 205],
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 연도별 참가국 수 시각화
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Countries"], marker='o')
plt.title("Number of Countries Participating in the Olympics by Year")
plt.xlabel("Year")
plt.ylabel("Number of Countries")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 표시
plt.show()