class SmartHouse:
    def __init__(self, temerature_pm: int, is_light_on_pm: bool):
        self.__temperature = temerature_pm
        self.is_light_on = is_light_on_pm

    def increase_temperature(self):
        if self.__temperature < 40:
            self.__temperature += 1

    def set_temperature(self, temperature_pm: int):
        if temperature_pm > 40:
            temperature_pm = 40
        elif temperature_pm < 12:
            temperature_pm = 12

        self.__temperature = temperature_pm

    def decrease_temperature(self):
        if self.__temperature > 12:
            self.__temperature -= 1

    def turn_light_on(self):
        self.is_light_on = True

    def turn_light_off(self):
        self.is_light_on = False


house = SmartHouse(25, True)

