import numpy
import copy

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for degree in self.coeff:
            s += self.coeff[degree]*x**degree
        return s

    def __add__(self, other):
        """Return self + other as Polynomial object."""
        result_coeff = copy.deepcopy(self.coeff)
        for key in other.coeff:
            if key in self.coeff:
                result_coeff[key] = result_coeff[key] + other.coeff[key]
            else:
                result_coeff[key] = other.coeff[key]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        result_coeff = {}
        for keyself in self.coeff:
            for keyother in other.coeff:
                if keyself + keyother in result_coeff:
                    result_coeff[keyself+keyother] = result_coeff[keyself+keyother] + self.coeff[keyself] * other.coeff[keyother]
                else:
                    result_coeff[keyself+keyother] = self.coeff[keyself] * other.coeff[keyother]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        #s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s

    

def test_Polynomial():
    p1 = Polynomial({1:1, 100:-3})
    p2 = Polynomial({20:1, 1:-1, 100:4})
    assert (p1.__add__(p2)).coeff == {1:0, 20:1, 100:1}, 'Improper addition.'
    assert(p1.__mul__(p2)).coeff == {2:-1, 21:1, 101:7, 120:-3, 200:-12}, 'Improper multiplication.'
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'verify':
        test_Polynomial()