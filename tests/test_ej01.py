import pytest
from src.ej01_def import saludar

@pytest.mark.parametrize(
    "nombre, expected",
    [
        ("Juán", "Hola, Juán"),
        ("012", "Hola, 012"),
        ("juanito el fantasía", "Hola, juanito el fantasía")
    ]
)
def test_saludar(nombre, expected):
    assert saludar(nombre) == expected