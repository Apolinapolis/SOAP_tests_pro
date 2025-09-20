import allure


@allure.feature('SOAP')
class TestSoap:

    def test_country_name(self, soap_session):
        with open('country_phone_code.xml', 'r', encoding='utf-8') as f:
            payload = f.read()
        response = soap_session.request(method='POST', data=payload)

        assert response.status_code == 200