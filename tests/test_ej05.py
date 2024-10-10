import pytest
from src.ej05_def2 import calcular_con_iva

@pytest.mark.parametrize(
    "importe_sin_iva, iva, expected",
    [
        (100, 10, "El precio final del artículo con IVA 10.00 es 110.00€"),
        (100, 110, "El precio final del artículo con IVA 21.00 es 121.00€"),
        (100, -10, "El precio final del artículo con IVA 21.00 es 121.00€")
    ]
)
def test_calcular_con_iva(importe_sin_iva, iva, expected):
    assert calcular_con_iva(importe_sin_iva, iva) == expected