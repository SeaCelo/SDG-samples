from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time


# Define a list of Sustainable Development Goals
sustainable_goals = [
    "No Poverty",
    "Zero Hunger",
]

# Loop through each Sustainable Development Goal
for i, goal in enumerate(sustainable_goals):
    # Define the search query by appending "Sustainable Development Goal" to the goal name, and excluding Wikipedia
    # query = f"{goal} Sustainable Development Goal -site:wikipedia.org site:*.org"
    query = f"{goal} Sustainable Development Goal"
    print(query)

    # Make a request to Google and retrieve the search results
    search_results = search(query, num_results=20)

    # Filter the search results to only include URLs ending in ".org"
    filtered_results = [
        url for url in search_results if ".org" in url and "wikipedia" not in url
    ][:10]

    # Loop through each filtered search result and scrape its content
    for url in filtered_results:
        print(f"Downloading {url}...")
        # Code to scrape the content of the URL goes here

    # Wait for 2 seconds before making the next request
    time.sleep(2)
