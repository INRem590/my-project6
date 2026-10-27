#тесты для тестового калькулятоар
import pytest
from calculator import add, subtract, multiply, divide


class TestCalculator:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
    def test_add_mixed_numbers(self):
        assert add(-1, 5) == 4
    def test_subtract_positive(self):
        assert subtract(5, 3) == 2
    def test_subtract_negative_result(self):
        assert subtract(3, 5) == -2

    def test_multiply_positive(self):
        assert multiply(4, 3) == 12
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
    def test_multiply_negative(self):
        assert multiply(-2, -3) == 6

    def test_divide_positive(self):
        assert divide(10, 2) == 5
    def test_divide_with_remainder(self):
        assert divide(7, 2) == 3.5
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Ошибка! Деление на ноль недопустимо."):
            divide(10, 0)