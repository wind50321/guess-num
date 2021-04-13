import random

answer = random.randint(1, 100) #產生隨機整數，包含1和100
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜數字： ')
    num = int(num)
    print('猜第', count, '次')
    if num == answer:
        print('你猜對了！')
        break
    else:
        if num > answer:
            print('比答案大')
        else:
            print('比答案小')