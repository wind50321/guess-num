import random

start = input('請決定隨機數字範圍開始值： ')
end = input('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)

answer = random.randint(start, end)
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