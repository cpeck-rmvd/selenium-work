from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import deque

# Program to win the "Wikipedia Game" -- find the minimum number of link clicks needed to navigate from one Wikipedia article to another

def find_degrees_of_separation(search_term1, search_term2):
    driver = webdriver.Firefox()
    driver.get("https://www.wikipedia.org/")
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys(search_term1)
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()
    search_result = driver.find_element(By.XPATH, "//div[@class='mw-search-results']/ul/li[1]/div/a")
    link1 = search_result.get_attribute("href")
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys(search_term2)
    search_button.click()
    search_result = driver.find_element(By.XPATH, "//div[@class='mw-search-results']/ul/li[1]/div/a")
    link2 = search_result.get_attribute("href")
    # Keep track of visited pages
    visited = set()
    visited.add(link1)
    # Create a queue to store the pages to visit
    queue = deque([link1])
    degree = 0
    while queue:
        degree += 1
        # Get the next page to visit
        current_page = queue.popleft()
        # Get all the links on the page
        links = driver.find_elements(By.XPATH, "//div[@id='mw-content-text']//a[@href]")
        for link in links:
            # Get the href attribute of the link
            href = link.get_attribute("href")
            # Check if the link leads to a Wikipedia article
            if "wikipedia.org" in href and "wiki" in href:
                if href not in visited:
                    visited.add(href)
                    queue.append(href)
                    if href == link2:
                        driver.close()
                        return degree
    driver.close()
    return -1

search_term1 = input("Enter the first Wikipedia search term: ")
search_term2 = input("Enter the second Wikipedia search term: ")
degree = find_degrees_of_separation(search_term1, search_term2)
if degree == -1:
    print("The two articles are not connected.")
else:
    print(f"The degrees of separation between the two articles is {degree}.")
