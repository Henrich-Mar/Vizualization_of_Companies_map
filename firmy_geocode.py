import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load your dataset from the Excel file
data = pd.read_excel('dataset_firiem.xlsx')

# Create a map centered on a specific location (you can adjust the coordinates and zoom level)
m = folium.Map(location=[48, 17], zoom_start=10)

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)


# Loop through the dataset and add markers for each company
for index, row in data.iterrows():
    company_name = row['Názov']
    latitude = row['Latitude']
    longitude = row['Longitude']
    revenue = row['Tržby']  # Assuming you have a column named "Total Revenue" in your dataset
    
    # Customize the marker popup content
    popup = f"{company_name}<br>Výnos: {revenue:,.2f}".replace(',',' ')
    
    folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)

# Save the map to an HTML file
m.save('company_map.html')
