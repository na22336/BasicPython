from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

value = 0
N = 100
a = 0
b = pi/2
h = (b - a)/N
for i in range(100):
    value += h*(sin(0 + i * h) + sin(0 + (i + 1)*h))/2
print(value)
