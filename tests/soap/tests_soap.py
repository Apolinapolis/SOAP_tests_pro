import allure

from templates.read_templates import iso_code_xml_creator, xsd_response_creator


@allure.feature('SOAP')
class TestSoap:

    def test_country_name(self, soap_session):
        response = soap_session.request(method='POST', data=iso_code_xml_creator('IT'))
        assert iso_code_xml_creator
        assert response.status_code == 200

        xsd_response_creator('CountryNameResponse').validate(response.text)