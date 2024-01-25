
import streamlit as st
import geopandas as gpd
import folium 
from streamlit_folium import folium_static
import pathlib


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

cfd = pathlib.Path(__file__).parent
# Read GeoJSON file
geojson_path = cfd / 'ancient_empires.geojson'



# create GeoDataFrame
gdf = gpd.read_file(geojson_path)

# Create a Streamlit app with a dropdown bar
st.title("Select An Empire")
selected_empire = st.selectbox("Select an Empire", gdf['Empire'].tolist())

# Set the size of the map display
map_height = 1000
st.title("World Map")
m = folium.Map(location=[0, 0], zoom_start=5, control_scale=True, height=map_height)


#add function to pull geojson data based on select box.
def plot_geojson():
    selected_gdf = gdf[gdf['Empire'] == selected_empire]
    
    #center map around selected geodataframe
    center_lat, center_lon = selected_gdf.geometry.centroid.y.mean(), selected_gdf.geometry.centroid.x.mean()
    m.location = [center_lat, center_lon]
# Iterate through GeoJSON features and add them to the map
    for feature in selected_gdf.iterfeatures():
        geojson_feature = folium.GeoJson(feature, name=selected_empire)
        
        # Convert negative years to BC
        start_date = -feature['properties']['Starting_Date']
        end_date = -feature['properties']['End_Date']
        
        # Create a formatted tooltip with line breaks
        tooltip_text = f"<b>Empire:</b> {feature['properties']['Empire']}<br>" \
                       f"<b>Start Date:</b> {start_date} BC<br>" \
                       f"<b>End Date:</b> {end_date} BC"
        
        folium.Popup(tooltip_text, max_width=300).add_to(geojson_feature)  # Adjust max_width as needed
        
        geojson_feature.add_to(m)

plot_geojson()
    
#tooltip = 'This is a placeholder tooltip'



folium_static(m)
