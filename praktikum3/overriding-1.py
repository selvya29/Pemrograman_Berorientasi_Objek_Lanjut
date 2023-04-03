class Animal:
    def speak(self):
        print("The animal makes a sound")

class Mouse(Animal):
    def speak(self):
        print("The mouse squeak")

class Snake(Animal):
    def speak(self):
        print("The snake hisses")

animal = Animal()
animal.speak()  # Output: The animal makes a sound

mouse = Mouse()
mouse.speak()  # Output: The mouse squeak

snake = Snake()
snake.speak()  # Output: The snake hisses