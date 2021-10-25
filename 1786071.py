# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:36:29 2021

@author: Geon Yuk
"""
#1. Up&down 
import random
num = random.randint(1,101)
count = 0

while True:
    count += 1
    usr = int(input('1부터 100사이의 난수를 맞추세요. : '))
    if usr == num:
        print('정답입니다.')
        break
    
    elif num > int(usr):
        print('틀렸습니다. 생각한 숫자는 더 큰 숫자 입니다.')
    else:
        print('틀렸습니다. 생각한 숫자는 더 작은 숫자 입니다.')
        
    if count == 10:
        print('게임에 졌습니다. , 정답은 %d 입니다'%num)
        break


#2. 사각형의 넓이 구하기
count = 1
maxArea = 150

while True:
    result = ((count*2) * (count*3))
    if result > maxArea: break
    print('사각형의 넓이 :', result)
    count += 1

print('가장 작은 사각형의 넓이 : 6')
print('가장 큰 사각형의 넓이 : 150' )     