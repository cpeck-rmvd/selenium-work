with open("selenium.py", "r") as file: text = ["from selenium.webdriver.common.by import By"] + file.readlines()
for i in range(len(text)): text[i].replace("_by_css_selector(", "(By.CSS_SELECTOR").replace("_by_xpath(", "(By.XPATH").replace("_by_name(", "(By.NAME").replace("_by_link_text(", "(By.LINK_TEXT").replace("_by_partial_link_text(", "(By.PARTIAL_LINK_TEXT").replace("_by_tag_name(", "(By.TAG_NAME").replace("_by_class_name(", "(By.CLASS_NAME")
with open("selenium4.py", "w") as file: file.writelines(text)
