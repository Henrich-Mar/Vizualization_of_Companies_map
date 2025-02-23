# Company Revenue Map Visualization

This project creates interactive maps visualizing company revenues across different locations using Python, Folium, and geocoding services.

## Overview

The project consists of several scripts that:
1. Convert company addresses to geographical coordinates
2. Generate interactive HTML maps showing company locations
3. Visualize revenue data through color-coded markers and clusters

## Features

- **Geocoding**: Converts company addresses to latitude/longitude coordinates using Bing Maps API
- **Interactive Maps**: Creates web-based maps using Folium
- **Revenue Visualization**: 
  - Shows individual company locations with revenue information
  - Creates clusters that aggregate revenues for nearby companies
  - Color-coded markers based on revenue thresholds
- **Dual View Option**: Ability to toggle between revenue amounts and company count views
- **Region Highlighting**: Supports highlighting specific regions (e.g., Trnavský kraj, Trenčiansky kraj)

## Prerequisites

- Python 3.x
- Required Python packages:
  ```
  pandas
  folium
  requests
  ```
- Bing Maps API key (for geocoding)

## File Structure

- `Convert_tn_tt.py`: Geocoding script that converts addresses to coordinates
- `Firmy_tn_tt.py`: Generates single-view revenue map
- `Firmy_tn_tt Dual_map.py`: Creates dual-view map with revenue and company count options
- `dataset_tn_tt.xlsx`: Input data file
- `geocoded_dataset_TN_TT.xlsx`: Processed data with coordinates
- `kraje.json`: GeoJSON file for region boundaries

## Usage

1. First, run the geocoding script to convert addresses:


2. Then generate the map using either:
python Firmy_tn_tt.py # For single view
or
python "Firmy_tn_tt Dual_map.py" # For dual view


3. Open the generated HTML file in a web browser to view the interactive map

## Map Features

- **Markers**: Each company is represented by a marker
- **Popups**: Click markers to see company details:
  - Company name
  - Revenue
  - Address
- **Clusters**: Companies in close proximity are grouped into clusters
- **Revenue Display**: Cluster icons show the sum of revenues for contained companies
- **Color Coding**: 
  - Red markers: Higher revenue companies
  - Yellow markers: Lower revenue companies

## Configuration

The maps can be customized by modifying:
- Initial map center coordinates
- Zoom level
- Marker colors and styles
- Cluster appearance and behavior
- Region highlighting colors


## Contributors

Ing. Henrich Marcinov