class MobilePhone:
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f'mobile phone {self.model} is turned on'

    def turn_off(self):
        return f'mobile phone {self.model} is turned off'

    def call_number(self, number):
        return f'calling {number} from {self.model}'


mob_phone1 = MobilePhone('Samsung S22')
mob_phone2 = MobilePhone('iPhone16')

assert mob_phone1.turn_on() == 'mobile phone Samsung S22 is turned on'
assert mob_phone2.turn_on() == 'mobile phone iPhone16 is turned on'

assert mob_phone1.call_number('011-222-3333') == 'calling 011-222-3333 from Samsung S22'
assert mob_phone2.call_number('011-222-4444') == 'calling 011-222-4444 from iPhone16'

assert mob_phone1.turn_off() == 'mobile phone Samsung S22 is turned off'
assert mob_phone2.turn_off() == 'mobile phone iPhone16 is turned off'
