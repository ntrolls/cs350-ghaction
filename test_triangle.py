from triangle import triangle

def test_invalid1():
    assert triangle(-1, 0, 1) == -1

def test_equilateral():
    assert triangle(4, 4, 4) == 2