# About My Project

Student Name:  Daniel Chmielewski
Student Email:  dachmiel@syr.edu

### What it does
This project visualizes college football quarterback passing statistics from the CollegeFootballData API. It allows users to select a specific year from a dropdown and either load previously saved data if it already exists in the cache or retrieve it from the API. Once loaded, users can view the top N passers ranked by yards, completions, or attempts, which are displayed both as a sortable table and a Plotly bar chart. The dashboard also calculates and displays the average passing stats across all players for the selected year.

### How you run my project
1. Run "uv pip install -r requirements.txt --system" in the terminal
2. Run main.py using streamlit to interact with the dashboard
3. Hit refresh data button to pull dataset into cache (based on the year chosen in the dropdown)

### Other things you need to know
