import pytest

from tasks_oop.equipment import Warehouse

data1 = [
    ("7785968391833", "Driver console", "M-2", "Ukraine",
     "ID:1, Barcode:7785968391833, Name:Driver console, Model:M-2, Manufacturer:Ukraine added successfully"
     )
]


@pytest.mark.parametrize("barcode, name, model, manufacturer, expected_result", data1)
def test_add_equipment(barcode, name, model, manufacturer, expected_result):
    """verify add_equipment method"""
    warehouse = Warehouse("Warehouse #1", "Test Street 2")
    assert warehouse.add_equipment(barcode, name, model, manufacturer) == expected_result
