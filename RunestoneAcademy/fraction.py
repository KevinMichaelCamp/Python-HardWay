class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def getDenominator(self):
        return self.denominator

    def getNumerator(self):
        return self.numerator

    def __str__(self):
        return "<Fraction object> {}/{}".format(self.numerator, self.denominator)

a = Fraction(5,2)
print(a)
