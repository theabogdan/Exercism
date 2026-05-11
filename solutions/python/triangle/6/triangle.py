def is_triangle(sides):
    side1, side2, side3 = sorted(sides)
    return side1 > 0 and side1 + side2 > side3


def equilateral(sides):
    if is_triangle(sides):
        if len(set(sides)) == 1:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    if is_triangle(sides):
        if len(set(sides)) <= 2:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if is_triangle(sides):
        if len(set(sides)) == 3:
            return True
        else:
            return False
    else:
        return False
