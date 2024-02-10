
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def print(self):
        print("\nx1 = ", self.x, " y1 = ", self.y)
        print("x2 = ", self.x+self.w, " y2 = ", self.y)
        print("x3 = ", self.x, " y3 = ", self.y+self.h)
        print("x4 = ", self.x+self.w, " y4 = ", self.y+self.h)
    
class Quad:
    def __init__(self,x,y,a):
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

obj1 = Rectangle(3,3,3,4)
obj2 = Quad(1,1,1)
obj1.print()
obj2.print()
obj2.print()
print("\nIntersection:", is_intersect(obj1, obj2))