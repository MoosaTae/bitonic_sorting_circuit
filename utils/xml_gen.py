import re
from lxml import etree

# create empty set in python
def increment_value(value_str):
    match = re.match(r'([a-zA-Z]+)(\d+)', value_str)
    if match:
        prefix, num = match.groups()
        new_num = int(num)
        if prefix == 'c':
            prefix = 'C'
        
        print(f"Incremented value: {value_str} -> {prefix}{new_num} at {pos.get('x')}, {pos.get('y')}")
        return f"{prefix}{new_num}"
    else:
        print(f"Failed to increment value: {value_str}")
        return value_str
    
def get_name(value_str):
    match = re.match(r'([a-zA-Z]+)(\d+)', value_str)
    if match:
        prefix, num = match.groups()
        return prefix, int(num)
    else:
        return ""
    
name = 'main.dig'
tree = etree.parse(name)

# Iterate through all visualElement nodes
for visual_element in tree.xpath('//visualElement'):
    pos = visual_element.find('pos')
    if pos is not None and (int(pos.get('x')) < -7400) and int(pos.get('y')) != -1:
        element_attributes = visual_element.find('elementAttributes')
        if element_attributes is not None:
            for entry in element_attributes.findall('entry'):
                label = entry.findall('string')
                if label[0].text == 'NetName':
                    label[1].text = increment_value(label[1].text)
                    # name, number = get_name(label[1].text)
                    # if(name != "" and number % 2 == 1):
                    #     print(f"Moved {name}{number}")

# Save the updated XML to a new file
tree.write(name)