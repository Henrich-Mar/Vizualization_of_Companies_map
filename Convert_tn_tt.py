import requests
import pandas as pd
import time

# Your Bing Maps API Key
BING_MAPS_API_KEY = 'Ajn6q7gKQTRlOkVH9WjOpTQ90wzTXmSS3fTacodRhOPfSpyak64m_3K8auCALZc3'

def geocode_bing(row):
    # Construct the full address from the three columns
    adresa = row.get('Adresa', '')
    mesto = row.get('Mesto', '')
    psc = row.get('PSČ', '')
    
    full_address = f"{adresa}, {mesto}, {psc}, Slovakia"
    
    base_url = "http://dev.virtualearth.net/REST/v1/Locations"
    params = {
        "query": full_address,
        "key": BING_MAPS_API_KEY,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    time.sleep(0.150)
    # Extract latitude and longitude from the response
    try:
        coordinates = data['resourceSets'][0]['resources'][0]['point']['coordinates']
        print(f"Processed: {full_address}- coords :{coordinates[0]}, {coordinates[1]}")

        return coordinates[0], coordinates[1]
    except (KeyError, IndexError):
        print(f"Failed to geocode: {full_address}")
        return None, None

# Load your dataset
df = pd.read_excel('dataset_tn_tt.xlsx')

# Geocode each address
df['Latitude'], df['Longitude'] = zip(*df.apply(geocode_bing, axis=1))

# Save the results
df.to_excel('geocoded_dataset_TN_TT.xlsx', index=False)
