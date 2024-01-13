
import streamlit as st
import plotly.express as px
import geopandas as gpd
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import matplotlib



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

# Read GeoJSON file
geojson_path = 'ancient_empires.geojson'

gdf = gpd.read_file(geojson_path) 


# Create a Streamlit app with a dropdown bar
st.title("Select An Empire")
selected_empire = st.selectbox("Select an Empire", gdf['Empire'].tolist())





# Display an empty map
st.title("World Map")
df = pd.DataFrame({'lat': [0.00], 'lon': [0.00]}) 
fig = px.scatter_geo()




# Display the selected empire
st.write(f"You selected: {selected_empire}")

# Filter GeoDataFrame based on the selected empire
selected_gdf = gdf[gdf['Empire'] == selected_empire]


# Create an empty map
fig = px.choropleth(selected_gdf, geojson=selected_gdf.geometry, locations=selected_gdf.index, projection="natural earth")
fig.add_trace(px.choropleth(geojson=selected_gdf.geometry, locations=[selected_gdf.index], projection="natural earth").data[0])
st.plotly_chart(fig)




#Work here
