class Shape:
    def __init__(self, shapes_list):
        # Initialize attributes for each shape type
        self.triangle = None
        self.square = None
        self.circle = None

        # Ensure the input is a list
        if not isinstance(shapes_list, list):
            raise TypeError(f"Expected a list, but got {type(shapes_list).__name__}")

        # Iterate through the list and assign to relevant class variable
        for shape in shapes_list:
            if isinstance(shape, Triangle):
                self.triangle = shape
            elif isinstance(shape, Square):
                self.square = shape
            elif isinstance(shape, Circle):
                self.circle = shape
            else:
                raise TypeError(f"Invalid shape type: {type(shape).__name__}")
    
    def display_shapes(self):
        return {
            "Triangle": self.triangle,
            "Square": self.square,
            "Circle": self.circle
        }


# Child classes
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


# Example usage
shapes = [Triangle(10, 5), Square(4), Circle(7)]
shape_obj = Shape(shapes)
print(shape_obj.display_shapes())

# Access individual shapes and their properties
if shape_obj.triangle:
    print("Triangle Area:", shape_obj.triangle.area())

if shape_obj.square:
    print("Square Area:", shape_obj.square.area())

if shape_obj.circle:
    print("Circle Area:", shape_obj.circle.area())
