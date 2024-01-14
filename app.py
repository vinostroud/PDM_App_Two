
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium 
from streamlit_folium import folium_static



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

# create GeoDataFrame
gdf = gpd.read_file(geojson_path)

# Create a Streamlit app with a dropdown bar
st.title("Select An Empire")
selected_empire = st.selectbox("Select an Empire", gdf['Empire'].tolist())

# Display an empty map
st.title("World Map")
m = folium.Map(location=[0, 0], zoom_start=5)

##new code here

# Function to display the selected empire
def display_selected_empire_map(selected_empire, gdf, map_object):
    # Iterate over map layers and remove them
    for layer_id in list(map_object._children):
        map_object._children.pop(layer_id)

    # Filter GeoDataFrame based on the selected empire
    selected_gdf = gdf[gdf['Empire'] == selected_empire]

    # Convert the GeoDataFrame to GeoJSON format
    geojson_data = selected_gdf.to_crs(epsg='4326').to_json()

    # Add the GeoJSON data to the map
    folium.GeoJson(
        geojson_data,
        name=selected_empire,
    ).add_to(map_object)

    # Display the map using st_folium
    folium_static(map_object)
    return st.write(f"You selected: {selected_empire}")

# Call the function
display_selected_empire_map(selected_empire, gdf, m)







