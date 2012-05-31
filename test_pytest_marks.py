import pytest

@pytest.marks('red', 'green', 'blue', 'black', 'orange', 'pink')
def test_something_1():
    assert 1 + 1 == 2

@pytest.marks('red')
def test_something_2():
    assert 2 + 2 == 4

@pytest.marks('red', 'green')
def test_something_3():
    assert 3 + 3 == 6

