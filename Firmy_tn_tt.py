import pandas as pd
import folium
from folium.plugins import MarkerCluster
import json
# Load your dataset from the Excel file
data = pd.read_excel('geocoded_dataset_TN_TT.xlsx')

# Create a map centered on a specific location
m = folium.Map(location=[48, 18], zoom_start=10)

# JavaScript function as a string
icon_create_function = """
function(cluster) {
    var markers = cluster.getAllChildMarkers();
    var totalRevenue = 0;
    for (var i = 0; i < markers.length; i++) {
        totalRevenue += parseFloat(markers[i].options.revenue);
    }
    var formattedRevenue = totalRevenue.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, "&nbsp;");
    var fontSize = (formattedRevenue.length <= 5) ? '14px' : (formattedRevenue.length <= 8) ? '12px' : '10px';
    return L.divIcon({
        html: '<div style="background-color:rgb(19, 255, 58);color:#000000;border-radius:100%;display:flex;align-items:center;justify-content:center;min-width:80px;padding:10px;font-size:' + fontSize + '"><span>' + formattedRevenue + '</span></div>',
        className: 'marker-cluster',
        iconSize: L.point(60, 60)
    });
}"""
# Create a marker cluster with the custom function
marker_cluster = MarkerCluster(icon_create_function=icon_create_function).add_to(m)

# Loop through the dataset and add markers for each company
for index, row in data.iterrows():
    company_name = row['Názov']
    latitude = row['Latitude']
    longitude = row['Longitude']
    revenue = row['Tržby']
    adresa = row['Adresa']
    mesto = row['Mesto']
    # Customize the marker popup content
    popup = f"{company_name}<br>Výnos: {revenue:,.2f}<br>Adresa: {adresa},{mesto}"
    
    folium.Marker(
        [latitude, longitude],
        popup=popup,
        icon=folium.Icon(iconColor='white'),
        revenue=str(revenue)  # Attach revenue as an option to the marker
    ).add_to(marker_cluster)



# Style function
def style_function(feature):
    """Return the style for each feature."""
    if feature['properties']['TXT'] == 'Trnavský kraj':
        return {
            'fillColor': '#FF0000',  # Red color
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6
        }
    elif feature['properties']['TXT'] == 'Trenčiansky kraj':
        return {
            'fillColor': '#0000FF',  # Blue color
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6
        }
    else:
        return {'fillOpacity': 0}

# Load GeoJSON data
with open("kraje.json", "r") as file:
    kraje_data = json.load(file)

# Add the GeoJSON data to the map
folium.GeoJson(
    kraje_data,
    name='geojson',
    style_function=style_function
).add_to(m)

# Save the map to an HTML file
m.save('company_map_tn_tt.html')
