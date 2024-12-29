<<<<<<< Updated upstream
from math import sin, pi,sqrt,exp
=======
from math import sin, pi, sqrt ,exp
>>>>>>> Stashed changes
# --example--
# print(sin(0))
# >>> 0
# -----------

<<<<<<< Updated upstream
def  trapezoidal_integral(f,a,b,n):
    value = 0
    h = (b - a)/n
    for i in range(n):
        value += h*(f(a + i * h) + f(a + (i + 1)*h))/2
    print(value)

# (1)
trapezoidal_integral(sin,0,pi/2,50)

# (2)
def secpi(x):
    return 4/(1 + x ** 2)

trapezoidal_integral(secpi,0,1,100)

# (3)
def rote(x):
    return sqrt(pi) * exp(-x**2)

trapezoidal_integral(rote,-100,100,1000)
=======
a = 0
b = 1
n = 100
def trapezoidal_integral(f,a,b,n):
    value = 0
    h = (b - a)/n
    for i in range(n):
        value += h*(f(0 + i * h) + f(0 + (i + 1)*h))/2
    return print(value)

# (1)

trapezoidal_integral(sin,0,pi/2,50)

# (2)
def second(x):
    return 4/(1 + x **2)

trapezoidal_integral(second,0,1,100)

# (3)
def third(x):
    return sqrt(x) * exp(- x **2)

trapezoidal_integral(third, -100 , 100, 1000)
>>>>>>> Stashed changes
