import pandas as pd

def load_passing_stats() -> pd.DataFrame:
    # Assuming data is loaded from a CSV or database
    # Adjust the path to wherever your CSV is stored
    df = pd.read_csv("cache/passing_stats.csv")
    return df

def top_passers(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    # Filter rows for passing yards (YDS), completions (COMPLETIONS), and attempts (ATT)
    passing_yards_df = df[df['statType'] == 'YDS']
    completions_df = df[df['statType'] == 'COMPLETIONS']
    attempts_df = df[df['statType'] == 'ATT']
    
    # Ensure the 'stat' column is numeric for sorting and calculations
    passing_yards_df['yards'] = pd.to_numeric(passing_yards_df['stat'], errors='coerce')
    completions_df['completions'] = pd.to_numeric(completions_df['stat'], errors='coerce')
    attempts_df['attempts'] = pd.to_numeric(attempts_df['stat'], errors='coerce')

    # Merge all dataframes on player and team
    df_merged = passing_yards_df[['player', 'team', 'yards']].merge(completions_df[['player', 'team', 'stat']], on=['player', 'team'], how='left')
    df_merged = df_merged.rename(columns={'stat': 'completions'})
    df_merged = df_merged.merge(attempts_df[['player', 'team', 'stat']], on=['player', 'team'], how='left')
    df_merged = df_merged.rename(columns={'stat': 'attempts'})
    
    # Sort by yards and get the top N players
    df_sorted = df_merged.sort_values(by='yards', ascending=False)
    
    return df_sorted[['player', 'team', 'yards', 'completions', 'attempts']].head(top_n)

def calculate_averages(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate averages for all players
    passing_yards_df = df[df['statType'] == 'YDS']
    completions_df = df[df['statType'] == 'COMPLETIONS']
    attempts_df = df[df['statType'] == 'ATT']

    # Convert 'stat' to numeric
    passing_yards_df['yards'] = pd.to_numeric(passing_yards_df['stat'], errors='coerce')
    completions_df['completions'] = pd.to_numeric(completions_df['stat'], errors='coerce')
    attempts_df['attempts'] = pd.to_numeric(attempts_df['stat'], errors='coerce')

    # Calculate averages
    avg_yards = passing_yards_df['yards'].mean()
    avg_completions = completions_df['completions'].mean()
    avg_attempts = attempts_df['attempts'].mean()

    return {
        "Average Yards": avg_yards,
        "Average Completions": avg_completions,
        "Average Attempts": avg_attempts
    }
