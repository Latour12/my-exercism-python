def equilateral(sides):
    if diff(sides) == 2:return True
    else: return False


def isosceles(sides):
    if diff(sides) >= 1:return True
    else: return False


def scalene(sides):
    if diff(sides) == 0: return True
    else: return False

def diff(sides):
    return len(sides) - len(set(sides))

def is_triangle(sides):
    