
# # Object-Oriented Programming: continuation
# # Algorithms and Data Structures
# # Big O Notation: constant - O(1), linear - O(n), quadratic - O(n^2), cubic - O(n^3), exponential - O(2^n), logarithmic - O(log n)

def greatest_common_divisor(a, b):
    while b != 0: 
        a, b = b, a % b
    return a

# Fraction class
# Implement: addition, equality, multiplication, division, subtraction, comparison operators(<, >)
class Fraction:

    def __init__(self, top, bottom):

        assert type(top) == int and type(bottom) == int, "top and bottom must be integers"

        self.top = top
        self.bottom = bottom

    def get_denominator(self):
        return self.bottom
    
    def get_numerator(self):
        return self.top

    def __str__(self):
        return str(self.top // greatest_common_divisor(self.top, self.bottom)) + "/" + str(self.bottom // greatest_common_divisor(self.top, self.bottom))
    
    # Addition
    def __add__(self, other_fraction):
        new_top = self.top * other_fraction.bottom + self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top , new_bottom)
    
    # Equality
    def __eq__(self, other_fraction):
        first_num = self.top * other_fraction.bottom
        second_num = self.bottom * other_fraction.top
        return first_num == second_num
    
    # Multiplication
    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top , new_bottom)
    
    # Division
    def __truediv__(self, other_fraction):
        new_top = self.top * other_fraction.bottom
        new_bottom = self.bottom * other_fraction.top
        return Fraction(new_top, new_bottom)
    
    # Subtraction
    def __sub__(self, other_fraction):
        new_top = self.top * other_fraction.bottom - self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top , new_bottom)
    
    # Comparison operators >
    def __gt__(self, other_fraction):
        first_num = self.top * other_fraction.bottom
        second_num = self.bottom * other_fraction.top
        return first_num > second_num
    
    # Comparison operators <
    def __lt__(self, other_fraction):
        first_num = self.top * other_fraction.bottom
        second_num = self.bottom * other_fraction.top
        return first_num < second_num


my_fraction = Fraction(1, 9)
my_fraction2 = Fraction(1, 4)

print(my_fraction + my_fraction2)