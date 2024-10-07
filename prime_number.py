a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

list1 = [a,b]
# （１）
import math
for j in list1:
    if type(j) == int and j >= 0:
        if j == 1:
            print('素数ではありません')

        elif all(j % i != 0 for i in range(2,round(math.sqrt(j)) + 1)):
            print('素数です')

        else:
             print('素数ですはありません')

    else:
         print('エラーを検出しました')



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
