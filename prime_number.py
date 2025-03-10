
import math
def prime(n):
    if type(n) == int and n > 0:
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif all(n % i != 0 for i in range(3,round(math.sqrt(n)) + 1 ,2)):
            return True
        else:
             return False
    else:

         print('エラーを検出しました')

a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# （１）
import math
if type(a) == int and a >= 0:
        if a == 1:
            print('aは素数ではありません')
            exit()
        elif all(a % i != 0 for i in range(2,round(math.sqrt(a)) + 1)):
            print('aは素数です')
            exit()
        else:
             print('aは素数ではありません')
             exit()
else:
         print('エラーを検出しました')
         exit()

# (2)
if type(b) == int and b >= 0:
        if b == 1:
            print('bは素数ではありません')
            exit()
        elif all(b% i != 0 for i in range(2,round(math.sqrt(a)) + 1)):
            print('bは素数です')
            exit()
        else:
             print('bは素数ではありません')
             exit()
else:
         print('エラーを検出しました')
         exit()


         return 'エラーを検出しました'


# 補遺
#for i in range(1,math.ceil(math.sqrt(b))):
    # if b == 1:
        # print('bは素数ではありません')
        # exit()

    # elif all(b % i != 0) == True:
        # print('bは素数です')
        # exit()
    
    #else:
