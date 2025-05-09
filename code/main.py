import streamlit as st
import pandas as pd
import plotly.express as px
from extract import fetch_passing_stats
from transform import load_passing_stats, top_passers, calculate_averages

# Set up the Streamlit dashboard
st.title("2024 College Football Passing Stats Dashboard")

# Load the passing stats from the cache
st.sidebar.header("Data Controls")
if st.sidebar.button("Refresh Data"):
    # Fetch new data from the API
    df = fetch_passing_stats()
    st.sidebar.success("Data refreshed successfully!")
else:
    df = load_passing_stats()

# Display the top passers
top_n = st.sidebar.slider("Top N Passers", min_value=5, max_value=50, value=10)
top_df = top_passers(df, top_n)

# Show the top passers in a table
st.subheader(f"Top {top_n} Passers by Yards in 2024")
st.write(top_df[["player", "team", "yards", "completions", "attempts"]])

# Visualize the top passers
fig = px.bar(top_df, x="player", y="yards", color="team", title=f"Top {top_n} Passers by Yards")
st.plotly_chart(fig)

# Calculate and show average stats
avg_stats = calculate_averages(df)
st.subheader("Average Passing Stats")
st.write(avg_stats)
