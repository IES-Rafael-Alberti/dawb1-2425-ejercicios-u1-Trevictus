import pytest
from src.ej02_def import calcular_salario

@pytest.mark.parametrize(
    "horas, precio_hora, expected",
    [
        (3.0, 2.0, 6.0),
        (2.5, 1.0, 2.5),
        (8.0, 5.0, 40.0),
        (12.0, 8.0, 96.0)
    ]
)
def test_calcular_salario(horas, precio_hora, expected):
    assert calcular_salario(horas, precio_hora) == expected