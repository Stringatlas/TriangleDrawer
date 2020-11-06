import math


SQRT = '√'

class Triangle:
    def all(self):
        return [*self.sides(), *self.angles(), self.area()]


class Sss(Triangle):
    def __init__(self, side1, side2, side3):  # given in right side, left side, bottom side
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def sides(self):
        return [self.side1, self.side2, self.side3]

    def angles(self):  # gets angles with law on cosines
        br_angle = math.degrees(math.acos((self.side1**2 + self.side3**2 - self.side2**2)/(2*self.side1*self.side3)))  # br = bottom right
        tp_angle = math.degrees(math.acos((self.side2**2 + self.side3**2 - self.side1**2)/(2*self.side2*self.side3)))  # tp = top
        bl_angle = 180 - br_angle - tp_angle                                                                           # bl = bottom left
        return [br_angle, bl_angle, tp_angle]  # br, tp, bl
    
    def area(self):  # gets area with herons formula
        semi = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(semi*(semi-self.side1)*(semi-self.side2)*(semi-self.side3))
        return area


class Asa(Triangle):
    def __init__(self, angle1, side1, angle2):  # given in br angle, bottom side, bl angle
        self.angle1 = angle1
        self.angle2 = angle2
        self.side1 = side1
        self.angle3 = 180 - self.angle1 - self.angle2

    def sides(self):  # gets two sides with law of sines
        bottomSide = self.side1
        rightSide = (bottomSide / math.sin(math.radians(self.angle3))) * math.sin(math.radians(self.angle1))
        leftSide = (bottomSide / math.sin(math.radians(self.angle3))) * math.sin(math.radians(self.angle2))

        print((bottomSide / math.sin(self.angle3)))
        self.side2 = rightSide
        self.side3 = leftSide

        return [leftSide, rightSide, bottomSide]

    def angles(self):
        return [self.angle1, self.angle3, self.angle2]  # br, tp, bl

    def area(self):
        rs, ls, bs = self.side1, self.side2, self.side3
        semi = (rs + ls + bs) / 2
        area = math.sqrt(semi * (semi - rs)*(semi - ls)*(semi - bs))

        return area


class Sas(Triangle):
    def __init__(self, side1, angle1, side2):  # given in: left side, bl angle, bottom side
        self.side1 = side1
        self.side2 = side2
        self.angle1 = angle1

    def sides(self):
        b = self.side1
        c = self.side2
        a = math.sqrt(b**2 + c**2 - 2*b*c * (math.cos(math.radians(self.angle1))))
        self.side3 = a

        return [b, a, c]

    def angles(self):
        a, b, c = self.side3, self.side1, self.side2
        bl_angle = self.angle1
        br_angle = math.degrees(math.acos((self.side1**2 + self.side3**2 - self.side2**2)/(2*self.side1*self.side3)))
        tp_angle = 180 - bl_angle - br_angle
        
        return [bl_angle, br_angle, tp_angle]  # br, tp, bl

    def area(self):
        a, b, c = self.side1, self.side2, self.side3
        semi = (a + b + c) / 2
        area = math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
        return area



class Aas(Triangle):  # br angle, tp angle, bottom side
    def __init__(self, angle1, angle2, side1):
        self.br_angle = angle1
        self.tp_angle = angle2
        self.bl_angle = 180 - self.br_angle - self.tp_angle
        self.bottomSide = side1

    def sides(self):
        self.rightSide = self.bottomSide * math.sin(math.radians(self.br_angle)) / math.sin(math.radians(self.tp_angle))
        self.leftSide = self.bottomSide * math.sin(math.radians(self.bl_angle)) / math.sin(math.radians(self.tp_angle))
        return [self.leftSide, self.rightSide, self.bottomSide]  # left side, right side, bottom side

    def angles(self):
        return [self.br_angle, self.tp_angle, self.bl_angle]

    def area(self):
        semi = (self.rightSide + self.leftSide + self.bottomSide) / 2
        area = math.sqrt(semi*(semi-self.rightSide)*(semi-self.leftSide)*(semi-self.bottomSide))
        return area



class Hl:
    def __init__(self, hypotonuse, leg): # leftside, bottom
        self.hypo = hypotonuse
        self.leg = leg
        self.leg2 = math.sqrt(self.hypo**2 - self.leg**2)
    def all(self):
        tri = Sss(self.leg2, self.hypo, self.leg)
        return tri.all()

