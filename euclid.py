# a = int(input("a の値を入力: "))
# b = int(input("b の値を入力: "))

# TODO
# while b!=0:
    # a, b  = b, a%b

# print(a)

class warizan:
    def euclid(a, b):
        while b!=0:
            a, b = b, a%b
        return print(a)
    
    def tagainiso(a, b):
        if warizan.euclid(a,b) == 1:
            return True
        else:
            return False
