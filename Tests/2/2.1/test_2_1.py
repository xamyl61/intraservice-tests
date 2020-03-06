# -*- coding: utf-8 -*-
import pytest
import requests


@pytest.fixture(scope="module")
def create_context(context_2_1):
    if context_2_1 != "NoParam":
        print("URL: ", context_2_1)
        r = requests.get('https://{}'.format(context_2_1))
        return r


def test_2_1_1():
    # assert 200 == create_context.status_code
    pass


def test_2_1_2():
    # assert 200 == create_context.status_code
    pass
