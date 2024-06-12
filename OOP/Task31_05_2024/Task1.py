class Car:
    def __init__(self, make_pm: str, model_pm: str, year_pm: int, mileage_pm: int):
        self.make = make_pm
        self.model = model_pm
        self.year = year_pm
        self.__mileage = mileage_pm

    def drive(self, distance: int) -> None:
        """Это метод для увеличения пробега """
        self.__mileage += distance

class Fleet:
    def __init__(self):
        self.__cars = []

    def add_car(self, car: Car) -> None:
        """Это метод для добавления автомобиля в автопарк"""
        self.__cars.append(car)

    def remove_car(self, make: str, model: str) -> None:
        """Это метод для удаления автомобиля по его марке и модели"""
        for item in self.__cars:
            if item.make == make and item.model == model:
                self.__cars.remove(item)

    def list_cars(self) -> None:
        """Это метод для вывода списка всех автомобилей в автопарке"""
        print(str(self.__cars))

mers = Car(make_pm="mersedes benz", model_pm="t-800", year_pm=1993, mileage_pm=1300)

authopark = Fleet()
authopark.add_car(mers)
authopark.list_cars()
authopark.add_car(mers)
authopark.list_cars()
authopark.add_car(mers)
authopark.list_cars()

