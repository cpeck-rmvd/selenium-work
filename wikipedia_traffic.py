import requests

def get_most_visited_pages(start_date, end_date, k):
    # Define the API endpoint
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top"
    # Define the parameters for the API call
    params = {
        "project": "en.wikipedia.org",
        "access": "all-access",
        "agent": "user",
        "start": start_date,
        "end": end_date,
        "limit": k
    }
    # Make the API call
    response = requests.get(url, params=params)
    # Get the JSON data from the API response
    data = response.json()
    # Get the list of most visited pages
    pages = data["items"][0]["articles"]
    # Print the k most visited pages
    for i, page in enumerate(pages):
        print(f"{i + 1}. {page['article']} - {page['views']} views")

start_date = input("Enter the start date (YYYYMMDD): ")
end_date = input("Enter the end date (YYYYMMDD): ")
k = int(input("Enterthe number of pages to retrieve: "))
get_most_visited_pages(start_date, end_date, k)


