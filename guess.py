import random

answer = random.randint(1, 100) #產生隨機整數，包含1和100
while True:
    num = input('請猜數字： ')
    num = int(num)
    if num == answer:
        print('你猜對了！')
        break
    else:
        if num > answer:
            print('比答案大')
        else:
            print('比答案小')