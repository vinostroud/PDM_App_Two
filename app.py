import streamlit as st
import plotly.express as px
import geopandas as gpd
import numpy as np
import plotly.figure_factory as ff
import pandas as pd

# List of empires
empires = [
    "Upper Egypt",
    "Old Kingdom of Egypt",
    "Akkadian Empire",
    "Indus Valley Civilisation",
    "Middle Kingdom of Egypt",
    "Xia dynasty",
    "Hyksos",
    "New Kingdom of Egypt",
    "Shang dynasty",
    "New Kingdom of Egypt",
    "Zhou dynasty",
    "Neo-Assyrian Empire",
    "Median Empire",
    "Achaemenid Empire",
    "Macedonian Empire",
    "Seleucid Empire",
    "Maurya Empire",
    "Han dynasty",
    "Xiongnu Empire",
    "Han dynasty"
]

# Create a Streamlit app with a dropdown bar
st.title("Empire Selector")
selected_empire = st.selectbox("Select an Empire", empires)

# Display the selected empire
st.write(f"You selected: {selected_empire}")

# Display an empty map
st.title("World Map")
df = pd.DataFrame({'lat': [0.00], 'lon': [0.00]}) 
fig = px.scatter_geo()

st.plotly_chart(fig)