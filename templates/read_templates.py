from jinja2 import Environment, select_autoescape, FileSystemLoader



env = Environment(
    loader= FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def iso_code_xml_creator(country_iso_code:str) -> str:
    template = env.get_template('/templates/xml/country_iso_code.xml')
    return template.render({'iso_code':country_iso_code})


