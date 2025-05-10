import requests
import pandas as pd

# Define the API key and headers for authentication
API_KEY = "P7xOVOuI/mnAXloKj28aJjcAnUFW3nRQ+fdgwdLjqQt1Xu0ODlblEhmNeKrEaoKe"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def fetch_passing_stats(year: int) -> pd.DataFrame:
    """
    Fetch passing stats from CollegeFootballData API and save to CSV.
    """
    url = f"https://apinext.collegefootballdata.com/stats/player/season?year={year}&category=passing"
    response = requests.get(url, headers=HEADERS)

    # # Debugging output
    # print("Status Code:", response.status_code)
    # print("Response Body Preview:", response.text[:300])

    response.raise_for_status()
    data = response.json()

    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(f"cache/passing_stats_{year}.csv", index=False)

    return df

if __name__ == "__main__":
    fetch_passing_stats()
