import logging
import random

import pytest



log = logging.getLogger('first_logger')


def test_first():
    assert True


def test_second(fixture_first):
    log.info(fixture_first)


@pytest.mark.parametrize('first_element', list(range(1, 5)))
@pytest.mark.parametrize('second_element', list(range(5, 10)))

def test_parametrization(first_element, second_element):
    log.info(f'{first_element} * {second_element} = {first_element * second_element}')



# Приклад використання фікстури у тесті
def test_using_fixture(my_fixture):
    print(f"Test with fixture value: {my_fixture}")
    assert my_fixture % 2 == 0
