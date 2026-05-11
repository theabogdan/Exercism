def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c


def equilateral(sides):
    if is_triangle(sides):
        if len(set(sides)) == 1:
            return "Equilateral"
        else:
            return None
    else:
        return "Not a triangle"


def isosceles(sides):
    if is_triangle(sides):
        if len(set(sides)) == 2:
            return "Isosceles"
        else:
            return None
    else:
        return "Not a triangle"


def scalene(sides):
    if is_triangle(sides):
        if len(set(sides)) == 3:
            return "Scalene"
        else:
            return None
    else:
        return "Not a triangle"
