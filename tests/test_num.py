import pytest

from usum import num


@pytest.mark.parametrize('value,result', [
    ('1', 1),
    ('0', 0),
    ('123', 123),
    ('123.45', 123.45),
    ('.3', .3),
    ('.0007', .0007),
    ('-1', -1),
    ('-123.45', -123.45),
])
def test_num(value, result):
    assert num(value) == result


def test_bad_value():
    with pytest.raises(ValueError):
        num('asdf')
