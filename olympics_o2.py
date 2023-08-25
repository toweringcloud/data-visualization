import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
df = pd.read_csv("olympics_participations_data.csv")

# Set up the Streamlit app layout
st.title("Olympics Participation Dashboard")

# Show the DataFrame
st.write("## Data")
st.dataframe(df)

# Display map using Plotly Express
st.write("## Map")
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
st.plotly_chart(fig)