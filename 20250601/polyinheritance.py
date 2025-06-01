class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Dog())
make_animal_speak(Cat())