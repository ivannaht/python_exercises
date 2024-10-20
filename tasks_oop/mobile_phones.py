class Device:
    count_of_devices = 0
    def __init__(self, model):
        self.model = model
        Device.count_of_devices += 1


class MobilePhone(Device):
    device = 'Mobile phone'
    count_of_phones = 0

    def __init__(self, model):
        super().__init__(model)
        self.__class__.count_of_phones += 1

    def turn_on(self):
        return f'{self.__class__.device} {self.model} is turned on'

    def turn_off(self):
        return f'{self.__class__.device} {self.model} is turned off'

    def call_number(self, number):
        return f'calling {number} from {self.model}'


mob_phone1 = MobilePhone('Samsung S22')
mob_phone2 = MobilePhone('iPhone16')
mob_phone2.owner = 'Emilia'

print('contents of mob_phone1:', mob_phone1.__dict__)
print('contents of mob_phone2:', mob_phone2.__dict__)
print('contents of class:', MobilePhone.__dict__)
print('Device category:', mob_phone1.__class__.device)

assert mob_phone1.turn_on() == 'Mobile phone Samsung S22 is turned on'
assert mob_phone2.turn_on() == 'Mobile phone iPhone16 is turned on'

assert mob_phone1.call_number('011-222-3333') == 'calling 011-222-3333 from Samsung S22'
assert mob_phone2.call_number('011-222-4444') == 'calling 011-222-4444 from iPhone16'

assert mob_phone1.turn_off() == 'Mobile phone Samsung S22 is turned off'
assert mob_phone2.turn_off() == 'Mobile phone iPhone16 is turned off'

assert MobilePhone.count_of_phones == 2
assert mob_phone2.owner == 'Emilia'

class Laptop(Device):
    device = 'Laptop'
    count_of_laptops = 0

    def __init__(self, model):
        super().__init__(model)
        self.__class__.count_of_laptops += 1

    def turn_on(self):
        return f'{self.__class__.device} {self.model} is turned on'

    def turn_off(self):
        return f'{self.__class__.device} {self.model} is turned off'

    def sell(self, owner):
        self.owner = owner


laptop1 = Laptop('ASUS Vivibook 15')
laptop2 = Laptop('Lenova IdeaPad Slim 3')
laptop3 = Laptop('Dell Inspiron 15')
laptop2.sell('Adelina')

print('contents of laptop1:', laptop1.__dict__)
print('contents of laptop2:', laptop2.__dict__)
print('contents of class:', Laptop.__dict__)
print('Device category:', laptop1.__class__.device)

assert Laptop.count_of_laptops == 3
assert laptop2.owner == 'Adelina'
assert Device.count_of_devices == 5
