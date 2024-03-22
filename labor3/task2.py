
class Rectangle:
    def __init__(self, x, y, w, h):
        if (w < 0 or h < 0):
            raise ValueError("Значения высоты и ширины должны быть +")
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def getX():
        return x
    def getY():
        return y
    def getH():
        return h
    def getW():
        return w
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setW(self, w):
        self.w = w
    def setH(self, h):
        self.h = h

    def print(self):
        print("\nx1 = ", self.x, " y1 = ", self.y)
        print("x2 = ", self.x+self.w, " y2 = ", self.y)
        print("x3 = ", self.x, " y3 = ", self.y+self.h)
        print("x4 = ", self.x+self.w, " y4 = ", self.y+self.h)
    
class Quad:
    def __init__(self,x,y,a):
        if a < 0:
            raise ValueError("Значение стороны должно быть +")
        self.x = x
        self.y = y
        self.a = a

    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def print(self):
        print("\nx1 = ", self.x, " y1 = ", self.y)
        print("x2 = ", self.x+self.a, " y2 = ", self.y)
        print("x3 = ", self.x, " y3 = ", self.y+self.a)
        print("x4 = ", self.x+self.a, " y4 = ", self.y+self.a)
        
def is_intersect(rect, quad):
    rect_x_range = range(rect.x, rect.x + rect.w + 1)
    rect_y_range = range(rect.y, rect.y + rect.h + 1)
    quad_x_range = range(quad.x, quad.x + quad.a + 1)
    quad_y_range = range(quad.y, quad.y + quad.a + 1)

    return any(x in quad_x_range and y in quad_y_range for x in rect_x_range for y in rect_y_range)

try:

    print("Введите значения x,y,w,h для прямоугольника: ")
    x = int(input("x: "))
    y = int(input("y: "))
    w = int(input("w: "))
    h = int(input("h: "))
    obj1 = Rectangle(x,y,w,h)

    print("Введите значения x,y,a для квадрата: ")
    x = int(input("x: "))
    y = int(input("y: "))
    a = int(input("w: "))
    obj2 = Quad(x,y,a)

    obj1.print()
    obj2.print()
    print("\nПересечение?:", is_intersect(obj1, obj2))
    obj2.move(-5,-5)
    obj2.print()
    print("\nПересечение?:", is_intersect(obj1, obj2))
except ValueError as e:
    print("Ошибка: ", str(e))