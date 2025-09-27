import xmlschema
from xmlschema import XMLSchema11
from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
XSD_DIR = os.path.join(TEMPLATE_DIR, "xsd")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))



def xml_iso_code_creator(country_iso_code:str) -> str:
    template = env.get_template('xml/country_iso_code.xml')
    return template.render({'iso_code':country_iso_code})


def xml_country_name_creator(country_name:str) -> str:
    template = env.get_template('xml/country_name.xml')
    return template.render({'country_name': country_name})


def xsd_response_creator(operation: str) -> XMLSchema11:
    envelop_xsd = env.get_template("xsd/envelope.xsd")
    rendered = envelop_xsd.render({"operation_xsd": f"{operation}.xsd", "operation": operation})
    temp_path = os.path.join(XSD_DIR, "temp.xsd")
    with open(temp_path, "w") as file:
        file.write(rendered)
    return xmlschema.XMLSchema11(temp_path)