import math

class Point:
    def __init__(self, InitX, InitY):
        self.x = InitX
        self.y = InitY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distanceFromPoint(self, Point):
        dX = self.x - Point.getX()
        dY = self.y - Point.getY()
        distance = math.sqrt(dX**2 + dY**2)
        return distance

    def reflect_x(self):
        return Point(-self.x, self.y)

    def slopeFromOrigin(self):
        if self.x == 0:
            return None
        M = (self.y/self.x)
        return M

    def slopeFromPoint(self, point):
        M = (self.y - point.getY()) / (self.x - point.getX())
        return M

    def equation_of_line(self, point):
        M = self.slopeFromPoint(point)
        B = -(M*self.x - self.y)
        return (M, B)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self

    def __str__(self):
        return "<Point object> x:{} y:{}".format(self.x, self.y)

def main():
    x1 = input("Enter x-coordinate > ")
    y1 = input("Enter y-coordinate > ")
    x2 = input("Enter x-coordinate > ")
    y2 = input("Enter y-coordinate > ")
    a =  Point(int(x1), int(y1))
    b =  Point(int(x2), int(y2))
    print("Your points are " + str(a) + " & " + str(b))
    distance = a.distanceFromPoint(b)
    print("The distance between the two points is " + str(distance))
    M, B = a.equation_of_line(b)
    print("The equation for the line containing these 2 points is y=" + str(M) + "x + " + str(B))

if __name__ == '__main__':
    main()
