# TODO
eps = 100000

while True:
    if 1 + eps > 1:
        eps = eps/2
    else:
        print(eps)
        break