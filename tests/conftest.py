import logging
import os
import random

import pytest
from dotenv import load_dotenv
from playwright.sync_api import APIRequestContext, expect, Playwright

log = logging.getLogger('first_logger')


@pytest.fixture(scope='class')
def fixture_first():
    log.info("First fixture")
    log.info("TEST START")
    value = random.choice(range(1000, 10000))
    yield value
    log.info("TEST FINISH")



@pytest.fixture(scope='session')
def fixture_start():
    log.info("==============TESTS START==============")

@pytest.fixture(scope='session', autouse=True)
def fixture_finish(fixture_start):
    yield
    log.info("==============TESTS FINISH==============")



@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return param_value * 2


logger = logging.getLogger('api')
@pytest.fixture()
def api_setup(playwright: Playwright):
    api = playwright.request.new_context(
        base_url=os.getenv('BASIC_URL'),
    )
    yield api

    api.dispose()

@pytest.fixture()
def api(api_setup: APIRequestContext):
    load_dotenv()
    payload = {
        'email': os.getenv('USER_LOGIN'),
        'password': os.getenv('USER_PASSWORD')
    }
    logger.info(f'Sending request to /api/auth/signin' )
    resp_login = api_setup.post(
        url='https://qauto.forstudy.space/api/auth/signin',
        data=payload
    )
    expect(resp_login).to_be_ok()


    yield api_setup
