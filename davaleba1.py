class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
      
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def get_full_name(self):
        """აბრუნებს სრულ სახელსა და გვარს."""
        return f"{self.first_name} {self.last_name}"

    def get_discount(self):
        """თუ ასაკი 18-ზე ნაკლებია, ამცირებს გადასახადს 20%-ით."""
        if self.age < 18:
            self.pay = self.pay * 0.8
        return self.pay

    def calculate_average(self):
        """ითვლის და აბრუნებს საშუალო ქულას."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        """ადგენს სტუდენტის სტატუსს საშუალო ქულის მიხედვით."""
        avg = self.calculate_average()
        
        if avg > 90:
            return "Excellent"
        elif 70 <= avg <= 90:
            return "Good"
        elif 50 <= avg < 70:
            return "Average"
        else:
            
            self.status = False
            return "Poor"


student1 = Student("გიორგი", "ბერიძე", 17, [40, 50, 45])

print(f"სტუდენტი: {student1.get_full_name()}")
print(f"ფასი ფასდაკლებამდე: 1000")
print(f"ფასი ფასდაკლების შემდეგ (ასაკი {student1.age}): {student1.get_discount()}")
print(f"საშუალო ქულა: {student1.calculate_average():.2f}")
print(f"შეფასება: {student1.get_status()}")
print(f"აქტიურია თუ არა სტატუსი: {student1.status}")