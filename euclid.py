# a = int(input("a の値を入力: "))
# b = int(input("b の値を入力: "))

# TODO
# while b!=0:
    # a, b  = b, a%b
#print

class Warizan:
    def euclid(a, b):
        while b!=0:
            a, b = b, a%b
        return a

    def tagainiso(a, b):
        if Warizan.euclid(a,b) == 1:
            return True
        else:
            return False

Warizan.tagainiso(14,91)