# Hello Streamlit

## streamlit dashboard from scratch

1. Search Code Templates : query codes for crawling & anayltics using ChatGPT
2. Collect Wiki & Location Data : troubleshoot code templates using Colab
3. Analyse Data : parse and aggregate collected data using Pandas and the like
4. Visualize Data : preview analysed location data as map view using Folium
5. Make Web UI : convert final result as web dashboard using Plotly & Streamlit
6. Store to Cloud : commit & push final code files into your public Github repo
7. Deploy to Cloud : launch web dashboard on Github repo with Streamlit Cloud

## streamlit local dashboard

1. pip -r requirements.txt
    > required python packages installed.
2. python olympics_c.py
    > olympics_c_result.json file created.
3. python olympics_i.py
    > olympics_i_result.csv file created.
4. python olympics_p.py
    > olympics_p_result.html file created.
    > ![Alt text](https://github.com/toweringcloud/hello-streamlit/blob/master/olympics_p_result.png)
5. python olympics_o1.py
    > Dash is running on http://127.0.0.1:8050
    > Serving Flask app 'olympics_o1'
    > ![Alt text](https://github.com/toweringcloud/hello-streamlit/blob/master/olympics_o1_result.png)
6. streamlit run olympics_o2.py
    > You can now view your Streamlit app in your browser.
    > Local URL: http://localhost:8501
    > ![Alt text](https://github.com/toweringcloud/hello-streamlit/blob/master/olympics_o2_result.png)

## streamlit cloud dashboard

https://hello-app-seswdfxhcft4ld9jagvdu6.streamlit.app

![Alt text](https://github.com/toweringcloud/hello-streamlit/blob/master/olympics_o2_result_map.png)
