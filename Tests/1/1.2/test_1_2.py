# -*- coding: utf-8 -*-
import pytest
import requests


@pytest.fixture(scope="module")
def create_context(context_1_2):
    if context_1_2 != "NoParam":
        print("URL: ", context_1_2)
        r = requests.get('https://{}'.format(context_1_2))
        return r

    # def resource_teardown():
    #     print("resource_teardown")
    # request.addfinalizer(resource_teardown)


def test_1_2_1(create_context):
    # assert 200 == create_context.status_code
    pass
