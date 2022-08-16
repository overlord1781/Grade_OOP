import pytest

def test_skip():
    pytest.skip('пропускаем тест')

def test_fail():
    pytest.xfail('ломанный тест')

def test_eq():
    assert type(123) == int