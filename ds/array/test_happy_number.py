from happy_number import happy_number


def test_happy_number():
    assert happy_number(1) is True
    assert happy_number(2147483646) is False
    assert happy_number(8) is False
