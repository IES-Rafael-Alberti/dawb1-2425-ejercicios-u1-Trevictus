import pytest
from src.ej04_def2 import conversion_celsius

@pytest.mark.parametrize(
    "farenheits, expected",
    [
        (34.00, "La temperatura en Celsius es 1.11ºC (34.00)"),
        (-12.00, "La temperatura en Celsius es -24.44ºC (-12.00)"),
        (78.00, "La temperatura en Celsius es 25.56ºC (78.00)")
    ]
)
def test_conversion_celsius(farenheits, expected):
    assert conversion_celsius(farenheits) == expected