import xmlschema
from xmlschema import XMLSchema11
from jinja2 import Environment, select_autoescape, FileSystemLoader



env = Environment(
    loader= FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def iso_code_xml_creator(country_iso_code:str) -> str:
    template = env.get_template('/templates/xml/country_iso_code.xml')
    return template.render({'iso_code':country_iso_code})


def xsd_response_creator(operation:str) -> XMLSchema11:
    envelop_xsd = env.get_template('./templates/xsd/envelope.xsd')
    country_iso_code_response = envelop_xsd.render(
        {'operation_xsd': f'{operation}.xsd', 'operation': operation})
    with open ('./templates/xsd/temp.xsd', 'w') as file:
        file.write(country_iso_code_response)
    return  xmlschema.XMLSchema11('./templates/xsd/temp.xsd')