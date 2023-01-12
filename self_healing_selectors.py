import re
from selenium.common.exceptions import NoSuchElementException
from cssselect import GenericTranslator

def self_heal_selector(driver, original_selector):
    try:
        element = driver.find_element_by_css_selector(original_selector)
        return element
    except NoSuchElementException:
        # Extract tag name, class name and id
        parsed_selector = GenericTranslator().css_to_xpath(original_selector)
        tag_name = parsed_selector.split("/")[-1].split("[")[0]
        class_name = None
        id_name = None
        if "class=" in parsed_selector:
            class_name = parsed_selector.split("class='")[1].split("'")[0]
        if "id=" in parsed_selector:
            id_name = parsed_selector.split("id='")[1].split("'")[0]

        # Create new selectors
        new_selectors = [f"{tag_name}"]
        if class_name:
            new_selectors.append(f"{tag_name}.{class_name}")
        if id_name:
            new_selectors.append(f"{tag_name}#{id_name}")

        # Try finding the element using new selectors
        for new_selector in new_selectors:
            try:
                element = driver.find_element_by_css_selector(new_selector)
                return element
            except NoSuchElementException:
                pass

        # Try finding the element using regular expressions
        for new_selector in new_selectors:
            new_selector = re.sub(r"\s*\[.*?\]", "", new_selector)
            try:
                element = driver.find_element_by_css_selector(new_selector)
                return element
            except NoSuchElementException:
                pass

        # Return error message or raise exception
        raise NoSuchElementException(f"Element not found using selector: {original_selector}")

