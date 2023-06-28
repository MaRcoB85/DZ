import xml.etree.ElementTree as ET
import json


def parse_element(element):
    locators = {}
    for locator_elem in element.findall('locator'):
        platform = locator_elem.get('platform')
        locator_type = locator_elem.get('locator_type')
        value = locator_elem.text
        locators[platform] = [locator_type, value]
    return locators


def parse_page(page_elem):
    page_data = {}
    for element_elem in page_elem.findall('element'):
        element_name = element_elem.get('name')
        locators = parse_element(element_elem)
        page_data[element_name] = locators
    return page_data


tree = ET.parse('file.xml')
root = tree.getroot()

data = {}

for page_elem in root.findall('page'):
    page_name = page_elem.get('name')
    page_data = parse_page(page_elem)
    data[page_name] = page_data

json_data = json.dumps(data, indent=4)

with open('file.json', 'w') as file:
    file.write(json_data)
