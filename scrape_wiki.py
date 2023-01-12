from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Wikipedia website
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find the search box element and enter the topic
search_box = driver.find_element_by_id("searchInput")
search_box.send_keys(input("Search Wikipedia for: ") + Keys.RETURN)

# Find the first heading
heading = driver.find_element_by_xpath("//h1[@class='firstHeading']").text

# Find the first paragraph
first_paragraph = driver.find_element_by_xpath("//div[@class='reflist']/p").text

# Print the information
print(f"Heading: {heading}")
print(f"First paragraph: {first_paragraph}")

# Close the browser
driver.close()
