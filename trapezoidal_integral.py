from math import sin, pi,sqrt,exp,cos
# --example--
# print(sin(0))
# >>> 0
# -----------

def  trapezoidal_integral(f,a = 0,b = 1,n = 100):
    value = 0
    h = (b - a)/n
    for i in range(n):
        value += h*(f(a + i * h) + f(a + (i + 1)*h))/2
    return float(value)

# (1)
print(trapezoidal_integral(sin,b = pi/2,n = 50))

# (2)
def secpi(x):
    return 4/(1 + x ** 2)

print(trapezoidal_integral(secpi,0,1,100))

# (3)
def rote(x):
    return sqrt(pi) * exp(-x**2)

print(trapezoidal_integral(rote,-100,100,1000))