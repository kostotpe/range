# range 範圍
# python 內建功能:可視為list產生器
# range 常跟 for loop  搭配，讓內容重複執行'固定次數'
import random

range(5) #[0, 1, 2, 3, 4] #不含結尾值 如5
range(3) #[0, 1, 2]

for i in range(3):
    print(3)
    print('hi')
for c in range(3):
    r = random.randint(1,100)
    print('這是第', c + 1, '次產生隨機數: ', r)

# 延伸
# range(起始值, 結束值)
# range(起始值,結束值,遞增值)
range(2, 5) # [2, 3, 4]
range(2, 10, 3) # [2, 5, 8]
range(3, 8, 2)
range(10, 3, -2) # [10, 8, 6, 4]

#線習寫一段程式碼來達到 印出 'hi' 一百次的功能

for i in range(100):
    print('hi')