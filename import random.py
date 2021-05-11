# python在安裝時預設的常用 標準函式庫 standard library--不用安裝，要使用時直接載入使用
# random --> 一個python檔案即為一個模組 module，很多模組封裝在一起稱為package/套件，放在一個資料夾內
import random

# 隨機產生包含1及100在內的一個整數
'''
r = random.randint(1, 100)
print(r)
'''

# 猜數字遊戲
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('請猜數字： ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        print('這是你猜的第 ', count, ' 次')
        break
    elif num > r:
        print('比答案大，請再猜')
    elif num < r:
        print('比簽案小，請再猜')
    print('這是你猜的第 ', count, ' 次')




