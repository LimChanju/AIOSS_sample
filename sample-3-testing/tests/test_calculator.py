"""계산기 테스트 (minimal)."""


def test_add_positive_numbers():
    from app.calculator import add
    assert add(2, 3) == 5


def test_subtract_positive_numbers():
    from app.calculator import subtract
    assert subtract(10, 3) == 7