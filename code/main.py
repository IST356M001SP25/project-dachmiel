import streamlit as st
import pandas as pd
import plotly.express as px
from extract import fetch_passing_stats
from transform import load_passing_stats, top_passers, calculate_averages
import os

st.title("College Football Passing Stats Dashboard")

year = st.sidebar.selectbox("Select Year", [2024, 2023, 2022, 2021, 2020])

csv_path = f"cache/passing_stats_{year}.csv"

# Load the passing stats from the cache or refresh data based on the selected year
st.sidebar.header("Data Controls")
# Handle data loading and refreshing
if st.sidebar.button("Refresh Data"):
    df = fetch_passing_stats(year=year)
    st.sidebar.success(f"Data for {year} refreshed successfully!")
elif os.path.exists(csv_path):
    df = load_passing_stats(year=year)
else:
    st.warning(f"No data found for {year}. Please click 'Refresh Data' to fetch it.")
    st.stop()  # Stop execution until data is available

# Stat filter
stat_filter = st.sidebar.selectbox(
    "Sort by Stat",
    ["yards", "completions", "attempts"]
)

# Filter top N players
top_n = st.sidebar.slider("Top N Passers", min_value=1, max_value=50, value=10)

# Display the top passers
top_df = top_passers(df, top_n, stat=stat_filter)

# Show the top passers in a table
st.subheader(f"Top {top_n} Passers by {stat_filter.capitalize()} in {year}")
st.write(top_df[["player", "team", "yards", "completions", "attempts"]])

# Visualize the top passers
fig = px.bar(top_df, x="player", y="yards", color="team", title=f"Top {top_n} Passers by {stat_filter.capitalize()} in {year}")
st.plotly_chart(fig)

# Calculate and show average stats for the selected year
avg_stats = calculate_averages(df)
st.subheader(f"Average Passing Stats in {year}")
st.write(avg_stats)
