import random


class Equipment:
    """
    class Equipment that creates piece of equipment.
    """

    equipment_id = 0

    def __init__(self, barcode, name, model, manufacturer):
        self.equipment_barcode = barcode
        self.equipment_name = name
        self.equipment_model = model
        self.equipment_manufacturer = manufacturer
        Equipment.equipment_id += 1


class Warehouse:
    """
    class Warehouse that stores equipment.
    """

    equipment_count = 0

    def __init__(self, name, address):
        self.warehouse_name = name
        self.warehouse_address = address
        self.equipment = []

    def add_equipment(self, barcode, name, model, manufacturer):
        # create an equipment object
        new_equipment = Equipment(barcode, name, model, manufacturer)
        self.equipment.append(new_equipment)
        Warehouse.equipment_count += 1
        return (
            f"ID:{new_equipment.equipment_id}, Barcode:{new_equipment.equipment_barcode}, "
            f"Name:{new_equipment.equipment_name}, Model:{new_equipment.equipment_model}, "
            f"Manufacturer:{new_equipment.equipment_manufacturer} added successfully")

    def show_warehouse_info(self):
        return (f"Name:{self.warehouse_name}, Address:{self.warehouse_address}, "
                f"Equipment count: {self.equipment_count} ")

    def show_equipment_list(self):
        print("List of equipment:")
        for item in self.equipment:
            print(
                f"ID:{item.equipment_id}, Barcode:{item.equipment_barcode}, "
                f"Name:{item.equipment_name}, Model:{item.equipment_model}, "
                f"Manufacturer:{item.equipment_manufacturer}")


warehouse1 = Warehouse("Warehouse #1", "Test Street 2")

barcodes = []

for n in range(10):
    code = random.randrange(1111111111111, 9999999999999)
    barcodes.append(code)

for barcode in barcodes:
    print(warehouse1.add_equipment(barcode, "Driver console", "M-2", "Ukraine"))

print(warehouse1.show_warehouse_info())

warehouse1.show_equipment_list()
