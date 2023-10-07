import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your weather data (replace 'your_dataset.csv' with the actual path to your CSV file)
data = pd.read_csv('weather Data.csv')

# Convert the 'Date/Time' column to a datetime format
data['Date/Time'] = pd.to_datetime(data['Date/Time'])

# Set the Streamlit app title
st.title('Weather Data Visualization')

# Sidebar filters
st.sidebar.header('Filters')

# Get the minimum and maximum dates from the dataset
min_date = data['Date/Time'].min().date()
max_date = data['Date/Time'].max().date()

# Allow the user to select a date within the range of your dataset using a slider
selected_date = st.sidebar.slider('Select Date', min_value=min_date, max_value=max_date, value=min_date)

selected_weather = st.sidebar.selectbox('Select Weather', data['Weather'].unique())

# Filter the data based on user selections
filtered_data = data[(data['Date/Time'].dt.date == selected_date) & (data['Weather'] == selected_weather)]

# Display the selected data
st.write(f"Displaying data for Date: {selected_date} and Weather: {selected_weather}")
st.write(filtered_data)

# Create a plot using Plotly (e.g., temperature vs. time)
st.header('Weather Data Visualization')

# Line chart for temperature vs. time
fig_temp = px.line(filtered_data, x='Date/Time', y='Temp_C', title=f'Temperature vs. Time for {selected_weather} on {selected_date}')
st.plotly_chart(fig_temp)

# Bar chart for relative humidity vs. time
fig_humidity = px.bar(filtered_data, x='Date/Time', y='Rel Hum_%', title=f'Relative Humidity vs. Time for {selected_weather} on {selected_date}')
st.plotly_chart(fig_humidity)

# Scatter plot for wind speed vs. visibility
fig_wind_visibility = px.scatter(filtered_data, x='Wind Speed_km/h', y='Visibility_km', title=f'Wind Speed vs. Visibility for {selected_weather} on {selected_date}')
st.plotly_chart(fig_wind_visibility)

# Create a 3D scatter plot for temperature, humidity, and visibility
fig_3d = go.Figure(data=[go.Scatter3d(
    x=filtered_data['Temp_C'],
    y=filtered_data['Rel Hum_%'],
    z=filtered_data['Visibility_km'],
    mode='markers',
    marker=dict(
        size=8,
        color=filtered_data['Wind Speed_km/h'],
        colorscale='Viridis',
        opacity=0.8
    ),
    text=filtered_data['Date/Time'],
    hoverinfo='text'
)])

fig_3d.update_layout(scene=dict(
    xaxis_title='Temperature (°C)',
    yaxis_title='Relative Humidity (%)',
    zaxis_title='Visibility (km)'
))

st.header('3D Scatter Plot')
st.plotly_chart(fig_3d)

# Additional visualizations
st.header('Additional Visualizations')

# Bar chart for weather distribution
weather_counts = data['Weather'].value_counts()
fig_weather_distribution = px.bar(weather_counts, x=weather_counts.index, y=weather_counts.values, title='Weather Distribution')
st.plotly_chart(fig_weather_distribution)

# Histogram for temperature distribution
fig_temp_histogram = px.histogram(data, x='Temp_C', nbins=20, title='Temperature Distribution')
st.plotly_chart(fig_temp_histogram)

# Pie chart for weather proportions
fig_weather_pie = px.pie(weather_counts, values=weather_counts.values, names=weather_counts.index, title='Weather Proportions')
st.plotly_chart(fig_weather_pie)










