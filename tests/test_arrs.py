from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -5, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == array_fixture[1:3]
    assert arrs.my_slice(array_fixture, 1) == array_fixture[1:]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(array_fixture, -10) == array_fixture
    assert arrs.my_slice(array_fixture, -2) == array_fixture[-2:]
