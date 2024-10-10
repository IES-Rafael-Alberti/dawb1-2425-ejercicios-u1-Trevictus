import pytest
from src.prueba1 import retornar_mayor

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (0, 0, 0),
        (4, 4, 0),
        (5, 8, 8),
        (9, 3, 9),
        (-1, -3, -1)
    ]
)
def test_retornar_mayor(num1, num2, expected):
    assert retornar_mayor(num1, num2) == expected