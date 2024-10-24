import requests
from bs4 import BeautifulSoup

# Define the URL and search query
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=그레이+데스페라도"

# Send a GET request to the page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant data in the soup object
    # Example: finding titles of search results
    results = soup.find_all('a', class_='title')

    # Print out only the search result titles
    for idx, result in enumerate(results):
        print(f"{idx + 1}. {result.get_text()}")
        # The line below that printed URLs has been removed
else:
    print(f"Failed to retrieve content. Status code: {response.status
