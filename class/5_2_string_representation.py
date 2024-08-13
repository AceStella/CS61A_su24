"""
Represents x divided by y
"""

class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + '/' + str(self.y)
    
    def __repr__(self):
        return "Fraction(" + str(self.x) + ',' + str(self.y) + ')'
    
one_half = Fraction(1, 2)
one_half
print(one_half)