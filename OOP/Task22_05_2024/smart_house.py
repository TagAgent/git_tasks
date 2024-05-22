class SmartHouse:
    def __init__(self, temerature_pm: int, is_light_on_pm: bool):
        self.temperature = temerature_pm
        self.is_light_on = is_light_on_pm

    def increase_temperature(self):
        if self.temperature < 40:
            self.temperature += 1

    def set_temperature(self, temperature_pm: int):
        if temperature_pm > 40:
            temperature_pm = 40
        elif temperature_pm < 12:
            temperature_pm = 12

        self.temperature = temperature_pm

    def decrease_temperature(self):
        if self.temperature > 12:
            self.temperature -= 1

    def turn_light_on(self):
        self.is_light_on = True

    def turn_light_off(self):
        self.is_light_on = False


house = SmartHouse(25, True)

print(house.temperature)
house.increase_temperature()
house.increase_temperature()
print(house.temperature)
house.decrease_temperature()
house.decrease_temperature()
house.decrease_temperature()
house.decrease_temperature()
print(house.temperature)
house.set_temperature(5000)
print(house.temperature)

print(house.is_light_on)
house.turn_light_off()
print(house.is_light_on)
house.turn_light_on()
print(house.is_light_on)

