import logging

import pytest

from common.apisession import TestSession
from common.project import config



@pytest.fixture(scope='module')
def soap_session():
    session = TestSession()
    session.base_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'
    session.headers.update({'Content-Type': 'application/soap+xml'})

    return session