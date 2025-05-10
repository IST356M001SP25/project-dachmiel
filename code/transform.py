import pandas as pd

def load_passing_stats(year: int) -> pd.DataFrame:
    """
    Load passing stats from a CSV file for a specific year.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(f"cache/passing_stats_{year}.csv")
    return df

def top_passers(df: pd.DataFrame, n: int, stat: str = "yards") -> pd.DataFrame:
    """
    Get the top N passers based on a given stat (yards, completions, or attempts).
    """
    # Filter rows for relevant stats (YDS, COMPLETIONS, ATT)
    df_filtered = df[df['statType'].isin(["YDS", "COMPLETIONS", "ATT"])]
    
    # Pivot the table to have columns for each stat
    df_pivot = df_filtered.pivot_table(index=["player", "team"], columns="statType", values="stat", aggfunc="first").reset_index()

    # Rename columns for consistency
    df_pivot.rename(columns={"YDS": "yards", "COMPLETIONS": "completions", "ATT": "attempts"}, inplace=True)

    # Convert the stats columns to numeric for sorting
    for col in ["yards", "completions", "attempts"]:
        df_pivot[col] = pd.to_numeric(df_pivot[col], errors="coerce")

    # Sort by the specified stat and return the top N passers
    df_sorted = df_pivot.sort_values(by=stat, ascending=False)
    return df_sorted.head(n)

def calculate_averages(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate average passing stats for the entire dataset.
    """
    # Filter data for relevant stat types
    passing_yards_df = df[df['statType'] == 'YDS'].copy()
    completions_df = df[df['statType'] == 'COMPLETIONS'].copy()
    attempts_df = df[df['statType'] == 'ATT'].copy()

    # Ensure numeric conversion for sorting and calculations
    passing_yards_df['yards'] = pd.to_numeric(passing_yards_df['stat'], errors='coerce')
    completions_df['completions'] = pd.to_numeric(completions_df['stat'], errors='coerce')
    attempts_df['attempts'] = pd.to_numeric(attempts_df['stat'], errors='coerce')

    # Calculate average stats
    avg_yards = passing_yards_df['yards'].mean()
    avg_completions = completions_df['completions'].mean()
    avg_attempts = attempts_df['attempts'].mean()

    # Create a DataFrame to contain the average stats
    avg_df = pd.DataFrame({
        "Stat": ["Yards", "Completions", "Attempts"],
        "Average": [avg_yards, avg_completions, avg_attempts]
    })

    # Round the average values to two decimal places
    avg_df["Average"] = avg_df["Average"].round(2)

    return avg_df
