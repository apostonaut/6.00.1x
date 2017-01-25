import math

def polysum(n, s):
    """Write a function called polysum that takes 2 arguments, n and s.
    This function should sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.

    :param n: The number of sides of the polygon
    :param s: The side length of the polygon
    :return: The sum of the (area) and the (square of the perimeter) of the polygon
    """

    perimeter = n * s
    #calculate the area
    area = ((0.25 * n * s**2) / math.tan(math.pi / n))

    #return the sum of the area and the square of the perimeter
    return round((area + perimeter**2), 4)

print (polysum(5, 10))