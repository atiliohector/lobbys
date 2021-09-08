import pytest

@pytest.fixture
def first_function():
    print('Print this fucking shit')
    a = 1
    assert a == 1
