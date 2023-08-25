import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# CSV 파일에서 데이터 불러오기
df = pd.read_csv("olympics_participations_data.csv")

# Dash 앱 초기화
app = dash.Dash(__name__)

# 지도 그래프 생성
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Participations",
    hover_name="Country",
    hover_data=["Participations"],
    projection="natural earth",
    title="Olympics Participation by Country",
)

# Dash 앱 레이아웃 설정
app.layout = html.Div(
    children=[
        html.H1("Olympics Participation by Country"),
        dcc.Graph(id="olympics-map", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)