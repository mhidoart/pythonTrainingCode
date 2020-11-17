class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def calculate_perimeter (self):
        return 2*(self.width + self.length)
    def what_am_i(self):
        print("I am a {}".format(type(self).__name__))

class Square(Shape):
    square_list = []
    def __init__(self,s1=2):
        self.s1 = s1
        self.square_list.append(self)
    def calculate_perimeter(self):
        return self.s1 *4
    def change_size(self,val):
        self.s1 += val
    def what_am_i(self):
        print("I am a {}".format(type(self).__name__))

rectangle = Rectangle(3,4)
square=Square(4)
print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())
square.change_size(-5)
print(square.calculate_perimeter())

square.what_am_i()
rectangle.what_am_i()
