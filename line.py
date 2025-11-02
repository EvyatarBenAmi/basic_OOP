class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__ (self):
        return f"point x: {self.x}, point y: {self.y}"
    
class Line:
    conter = 0
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        Line.conter += 1
    
    def show(self):
        print(f"point a: {self.a}, point b: {self.b}")

    @classmethod
    def how_many(cls):
        print(f"nomber in conter: {cls.conter}")

    @staticmethod
    def is_horizontal(line):
        return line.a.y == line.b.y 
        
if __name__ == "__main__":
    p1 = Point(5,8)
    p2 = Point(7,8)
    l = Line(p1, p2)
    l.show()
    l.how_many()
    print(l.is_horizontal(l))
    