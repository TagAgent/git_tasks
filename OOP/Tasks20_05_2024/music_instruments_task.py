class Instrument:
    def __init__(self, name_pm: str, cost_pm: int):
        self.name = name_pm
        self.cost = cost_pm

class Guitar(Instrument):
    def __init__(self, name_pm: str, cost_pm: int, number_of_strings_pm: int):
        super().__init__(name_pm, cost_pm)
        self.number_of_strings = number_of_strings_pm

    def play(self):
        "Этот метод для имитации игры на гитаре"
        print("Дрыньь!")

instrument1 = Instrument(name_pm="Фортопиано", cost_pm=15_000)
guitar1 = Guitar(name_pm="Басс гитара", cost_pm=8_000, number_of_strings_pm=4)
print(instrument1.name)
print(guitar1.play())