import pytest

from usum import group_by


def test_single_line():
    g = group_by(('a b 1',), (1, 2))
    assert len(g) == 1
    assert 'a b' in g
    assert g['a b'][0] == 1


def test_ordering():
    g = group_by(('a b 1',), (2, 1))
    assert 'b a' in g


def test_group():
    g = group_by([
        'a b 1',
        'b c 2',
        'a b 3',
        'b c 4',
        'd e 0',
    ], (1, 2))
    assert 'a b' in g
    assert 'b c' in g
    assert 'd e' in g
    assert len(g) == 3
    assert g['a b'] == [4]
    assert g['b c'] == [6]
    assert g['d e'] == [0]


def test_float():
    g = group_by([
        'a b 1.1',
        'b c 2',
        'a b 3',
    ], (1, 2))
    f = g['a b'][0]
    assert isinstance(f, float)
    assert f == 4.1
    assert g['b c'][0] == 2


def test_column_mismatch():
    with pytest.raises(Exception):
        group_by((
            'a b 1',
            'a b 1 2',
        ), (1, 2))
