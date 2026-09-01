import logging
import random

import pytest
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