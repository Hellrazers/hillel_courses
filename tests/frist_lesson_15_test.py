
import logging
import sys

import pytest

log = logging.getLogger('first_logger')

@pytest.mark.regression
@pytest.mark.first_mark
class DefultMarks:
    pass


@pytest.mark.api
class TestFirstClass(DefultMarks):
    def test_first(self):
        log.error('OUR START')
        assert True
        log.info('OUR FINISH')

    @pytest.mark.regression
    def test_frist_lesson(self):
        assert True


class TestSecondMarks(DefultMarks):


    def test_frist_lesson_15(self, fixture_first):
        assert True

    @pytest.mark.xfail(reason='somth problem in this taste not stabilitty')
    def test_xfail(self):
        assert False

    @pytest.mark.skip(reason='somth problem in this taste not stabilitty')
    def test_skip(self):
        assert False


    @pytest.mark.skipif(sys.platform == 'win32', reason='SKIP IF')
    def test_skipif(self):
        assert True