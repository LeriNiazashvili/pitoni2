class Employee:
    def __init__(self, name, salary):
        self.name = name

        if salary < 0:
            print(f"გაფრთხილება: {name}-ის ხელფასი არ შეიძლება იყოს უარყოფითი. მიენიჭა 0.")
            self.salary = 0
        else:
            self.salary = salary

    def show_info(self):
        print(f"თანამშრომელი: {self.name}, ხელფასი: {self.salary}")

    def work(self):
        print(f"{self.name}: Employee is working")

    def raise_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"{self.name}-ს ხელფასი გაეზარდა {amount}-ით. ახალი ხელფასი: {self.salary}")
        else:
            print("მატების რაოდენობა უნდა იყოს დადებითი!")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print(f"{self.name} is writing code in {self.programming_language}...")

    def work(self):
        print(f"{self.name}: Developer is coding")


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        print(f"{self.name} is creating design using {self.design_tool}...")

    def work(self):
        print(f"{self.name}: Designer is designing")




dev = Developer("გიორგი", 5000, "Python")

designer = Designer("ანი", 4500, "Figma")

print("--- Developer-ის ინფორმაცია ---")
dev.show_info()
dev.work()
dev.code()
dev.raise_salary(500)

print("\n--- Designer-ის ინფორმაცია ---")
designer.show_info()
designer.work()
designer.create_design()