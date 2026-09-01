import pathlib

BASE_DIR: pathlib.Path  = pathlib.Path(__file__).parent
LESSON_DIR: pathlib.Path = BASE_DIR.joinpath('lessons')
DATA_FOR_TEST_DIR: pathlib.Path = BASE_DIR.joinpath('data_for_tests')
