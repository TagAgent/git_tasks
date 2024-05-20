class Employee:
    def __init__(self, name_pm: str, seniority_pm: int):
        self.name = name_pm
        self.seniority = seniority_pm

    def upgrade_seniority(self) -> None:
        """"Это метод для повышения стажа сотрудника"""
        self.seniority += 1
        print(f"У сотрудника {self.name} повысился стаж")

    def introduce(self) -> None:
        """Это метод для вывода информации об сотруднике"""
        print(f"Здрастуйте меня зовут {self.name}\nМой стаж работы {self.seniority}")

class Manager(Employee):
    def fire(self, employee: Employee) -> None:
        """Это метод для увольнения сотрудника"""
        print(f"Сотрудник {employee.name} уволен менеджером {self.name}")

employee1 = Employee(name_pm="Джон", seniority_pm=12)
employee1.introduce()

employee2 = Employee(name_pm="Азамат", seniority_pm=1)
employee2.introduce()


employee3 = Employee(name_pm="Никита", seniority_pm=5)
employee3.introduce()

manager1 = Manager(name_pm="Джек", seniority_pm=17)
manager1.introduce()
manager1.fire(employee2)

manager2 = Manager(name_pm="Адольф", seniority_pm=3)
manager2.introduce()
manager2.fire(employee3)

manager2.upgrade_seniority()

employee1.upgrade_seniority()
