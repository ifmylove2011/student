from fractions import Fraction

def f(x):
    return 1+pow(3,pow(2,x))

l = map(f,[0,1,2,3,4,5])
for i in l:
    print(i)
# print(Fraction(0.5+sum(l))/pow(3,55))
#
# print(Fraction(1/2))
#
# print(Fraction(0.5/pow(3,9)))
