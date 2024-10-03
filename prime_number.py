a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)
# (1)
if a % 2 != 0 and a % 3 != 0  and a % 5 != 0 and a % 7 !=0:
    print('aは素数です')
else:
    print('aは素数ではありません')

# (2)
if b % 2 != 0 and b % 3 != 0  and b % 5 != 0:
    print('bは素数です')
else:
    print('bは素数ではありません')