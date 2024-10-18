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
