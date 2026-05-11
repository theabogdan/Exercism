def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c


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
        if len(set(sides)) == 2:
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
