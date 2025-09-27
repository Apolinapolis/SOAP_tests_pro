import xml.etree.ElementTree as ET



def check_value_result(expected_value:str, response_value:str) -> bool:
    root = ET.fromstring(response_value)
    return root[0][0][0].text == expected_value