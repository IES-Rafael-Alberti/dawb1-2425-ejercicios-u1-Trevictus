import pytest
from src.ej11_def import suma_primeros_enteros

@pytest.mark.parametrize(
    "num, expected",
    [
        (3, 6.0),
        (7, 28.0),
        (-6, 15.0),
        (0, 0.0)
    ]
)
def test_suma_primeros_enteros(num, expected):
    assert suma_primeros_enteros(num) == expected