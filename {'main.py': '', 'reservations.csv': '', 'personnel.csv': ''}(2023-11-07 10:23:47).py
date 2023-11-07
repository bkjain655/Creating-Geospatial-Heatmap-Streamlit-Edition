import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load data
reservations_data = pd.read_csv('reservations.csv')
personnel_data = pd.read_csv('personnel.csv')

# Merge data
merged_data = pd.merge(reservations_data, personnel_data, on='gate_id')

# Create map
m = folium.Map(location=[latitude, longitude], zoom_start=10)

# Create marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers
for index, row in merged_data.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(marker_cluster)

# Display map
st.title('Online Reservations Heatmap')
st.write('Mapped geographically against the number of workforce personnel manning gates')
st.write(m)