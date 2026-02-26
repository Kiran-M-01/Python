class Person:
    def speak(self):
        print("hi")
class Student(Person):
    def speak(self):
        super().speak()              # CALLING PARENT METHOD
        print("hello")
d = Student()
d.speak()
        