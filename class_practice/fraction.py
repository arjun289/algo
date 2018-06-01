class Fraction:
  def __init__(self, top, bottom):
    self.num = top
    self.den = bottom

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

  def __add__(self, sec):
    newnum = self.num*sec.den + self.den*sec.num
    newden = self.den*sec.den
    from fractions import gcd
    common_div = gcd(newnum, newden)
    return Fraction(newnum//common_div, newden//common_div)

