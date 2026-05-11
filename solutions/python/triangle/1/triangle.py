def triangle_type(a, b, c):
    """Calculate the triangle type."""
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a triangle"