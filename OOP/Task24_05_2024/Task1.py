class Human:
    def __init__(self, name_pm: str, age_pm: int, nationality_pm: str):
        self.name = name_pm
        self.age = age_pm
        self.nationality = nationality_pm

    def speak(self, words):
        print(words)


class Employee:
    def __init__(self, name_pm: str, seniority_pm: int, solary_pm: int):
        self.name = name_pm
        self.seniority = seniority_pm
        self.__salary = solary_pm

    def print_info(self):
        print(f"Имя: {self.name},\nСтаж: {self.seniority},\nЗП: {self.__salary}")
        print()

    def get_solary(self) -> int:
        return self.__salary

    def set_solary(self, salary: int) -> None:
        if salary > 0:
            self.__salary = salary


class Manager(Human):
    def increase_employee_salary(self, employee_obj: Employee, increase_percent: int) -> None:
        employee_obj.set_solary(self.__caclculate_new_salary())

    def __caclculate_new_salary(self, employee_obj: Employee, increase_percent: int) -> int:
        current_employee_salary = employee_obj.get_solary()
        new_employee_salary = current_employee_salary + (current_employee_salary / 100 * increase_percent)
        return new_employee_salary


employee0 = Employee(name_pm="Nikita", seniority_pm=10, solary_pm=20_000)
employee0.print_info()

employee0.set_solary(15_000)
print(employee0.get_solary())

employee0.set_solary(-50_000)
print(employee0.get_solary())
