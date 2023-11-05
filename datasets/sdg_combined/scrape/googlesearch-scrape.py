from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time

# Define a list of Sustainable Development Goals
sustainable_goals = [
    "No Poverty",
    "Zero Hunger",
    "Good Health and Well-being",
    "Quality Education",
    "Gender Equality",
    "Clean Water and Sanitation",
    "Affordable and Clean Energy",
    "Decent Work and Economic Growth",
    "Industry, Innovation and Infrastructure",
    "Reduced Inequalities",
    "Sustainable Cities and Communities",
    "Responsible Consumption and Production",
    "Climate Action",
    "Life Below Water",
    "Life On Land",
    "Peace, Justice and Strong Institutions",
    "Partnerships for the Goals",
]


# Loop through each Sustainable Development Goal
for i, goal in enumerate(sustainable_goals):
    # Define the search query by appending "Sustainable Development Goal" to the goal name, and excluding Wikipedia
    query = f"{goal} Sustainable Development Goal"
    print(query)

    # Make a request to Google and retrieve the first 20 search results
    search_results = search(query, num_results=30)

    # Keep only 20 results from ".org" and exclude wikipedia
    filtered_results = [
        url
        for url in search_results
        if ".org" in url and "wikipedia" not in url and "sdgcompass" not in url
    ][:20]

    # Define a list to store the text content of each URL
    text_content = []

    # Loop through each search result and scrape its content
    for url in filtered_results:
        print(f"Downloading {url}...")

        # Make a GET request to the URL with the user agent
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the main content section of the page
        content = (
            soup.find(id="content")
            or soup.find(id="main")
            or soup.find(id="bodyContent")
        )

        if content is None:
            print(f"No content found in {url}. Moving on...")
            continue

        # Remove any unwanted elements, such as images and links
        for element in content.find_all(["a", "img"], recursive=True):
            try:
                element.extract()
            except:
                pass

        # Extract the text from the remaining elements
        text = content.get_text()

        # Clean up the text by removing any extra whitespace
        text = " ".join(text.split())

        # Append the cleaned text to the list
        text_content.append(text)

        # Wait for 2 seconds before making the next request
        time.sleep(5)

    # Join the text content of each URL into a single string
    combined_text = "\n".join(text_content)

    # Write the combined text to a text file with the goal number as the filename
    filename = f"sdg-{i+1:02d}.txt"
    with open(filename, "w") as file:
        file.write(combined_text)
