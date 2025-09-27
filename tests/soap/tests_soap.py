from templates.read_templates import xml_iso_code_creator, xsd_response_creator, xml_country_name_creator
from templates.utils import check_value_result
import allure



@allure.feature('SOAP')
class TestSoap:

    def test_country_name(self, soap_session):
        response = soap_session.request(method='POST', data=xml_iso_code_creator('IT'))
        xsd_response_creator('CountryNameResponse').is_valid(response.text)
        assert response.status_code == 200
        assert check_value_result('Italy', response.text)


    def test_country_iso(self, soap_session):
        response = soap_session.request(method='POST', data=xml_country_name_creator('Italy'))
        xsd_response_creator('CountryISOCodeResponse').is_valid(response.text)
        assert response.status_code == 200
        assert check_value_result('IT', response.text)