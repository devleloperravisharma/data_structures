# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I make a sound")


# Child Class
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")


# Child Class
class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")


# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Display names
print("Dog's Name:", dog.name)
dog.speak()

print("Cat's Name:", cat.name)
cat.speak()