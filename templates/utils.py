import xml.etree.ElementTree as ET



def check_value_result(expected: str, response_value: str) -> bool:
    try:
        return ET.fromstring(response_value)[0][0][0].text == expected
    except (IndexError, AttributeError):
        return False