class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self):
        return self.score >= 5.0

    def introduce(self):
        print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")


students = [
    Student("An", 20, 8.5),
    Student("Binh", 21, 6.0),
    Student("Chi", 19, 4.5),
]

for s in students:
    s.introduce()
