# -*- coding: utf-8 -*-
import pytest
from Fixtures.application import Application


fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

