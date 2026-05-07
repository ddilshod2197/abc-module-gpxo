import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.sound())  # Woof!
print(cat.sound())  # Meow!
```

```python
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

square = Square(5)
circle = Circle(3)

print(square.area())  # 25
print(circle.area())  # 28.26
