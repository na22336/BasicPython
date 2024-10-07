a = input("aの値を入力:")
b = input("bの値を入力:")

# TODO
import math
a = int(a)
b = int(b)
# (1)
if a == 1:
    print('aは素数ではありません')
    exit()
elif a == 2 or a == 3 or a == 5 or a == 7:
    print('aは素数です')
    exit()

elif a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0:
        print('aは素数です')
        exit()

else:
        print('aは素数ではありません')
        exit()

# (2)
if b == 1:
    print('bは素数ではありません')
    exit()
elif b == 2 or b == 3 or b == 5 or b == 7:
    print('bは素数です')
    exit()

elif b % 2 != 0 and b % 3 != 0 and b % 5 != 0 and b % 7 != 0:
        print('bは素数です')
        exit()

else:
        print('bは素数ではありません')
        exit()


# 補遺
#for i in range(1,math.ceil(math.sqrt(b))):
    # if b == 1:
        # print('bは素数ではありません')
        # exit()

    # elif all(b % i != 0) == True:
        # print('bは素数です')
        # exit()

    # else:
        # print('bは素数ではありません')
        # exit()
