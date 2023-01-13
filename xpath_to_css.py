from lxml import etree

def xpath_to_css(xpath):
    # Parse the XPath expression
    xp = etree.XPath(xpath)
    # Get the first element of the parsed XPath
    element = xp.path[0]
    # Get the element name
    element_name = element.tag
    # Get the element's classes
    classes = element.attrib.get("class", "")
    css_selector = element_name
    if classes:
        css_selector += "." + ".".join(classes.split())
    # Iterate through the element's attributes
    for name, value in element.attrib.items():
        if name not in ["class", "id"]:
            css_selector += "[{}='{}']".format(name, value)
    return css_selector

xpath = "//div[@class='my-class' and @id='my-id']/span[@data-test='test-value']"
css_selector = xpath_to_css(xpath)
print(css_selector)
