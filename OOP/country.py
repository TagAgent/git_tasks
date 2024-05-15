class Country:
    def __init__(self, population_pm, territory_pm, whether_pm, language_pm):
        self.population = population_pm
        self.territory = territory_pm
        self.whether = whether_pm
        self.language = language_pm


USA = Country(population_pm=333_000_000, territory_pm=22_000_000, whether_pm="Солнечно", language_pm="Англиский")
Kyrgizstan = Country(population_pm=7_000_000, territory_pm=200_000, whether_pm="Жарко", language_pm="Кыгрызкий, Русский")

print(Kyrgizstan.territory)