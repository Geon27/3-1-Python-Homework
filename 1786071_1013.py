# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:30:40 2021

@author: Geon Yuk
"""
# 실전예제 1 - 출석부

students = ['정우람' , '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
print('시나리오 #1', students)
print('')

students.sort()
print('시나리오 #2', students)
print('')

students.remove('박찬호')
print('시나리오 #3', students)
print(len(students))
print('')

print('시나리오 #4', students[:3])
print('')

students.append('이병규')
students.sort()
print('시나리오 #5', students)
print('')

students.reverse()
print('시나리오 #6', students)
print('')

ind = students.index('정우람')
students[ind] = '정잘남'
print('시나리오 #7', students)

# 실전예제 2 -혈액 보관 시스템

boolds = []

for i in range(10):
    print('\헌혈해 주셔서 감사합니다. 헌혈하신 혈액형을 선택하세요')
    boolds.append(input('A, B, AB, O : '))
    
print('-' * 30)
print('혈액형 :', '개수')
print('-' * 30)
print('A형 :', boolds.count('A'))
print('B형 :', boolds.count('B'))
print('AB형 :', boolds.count('AB'))
print('O형 :', boolds.count('O'))
print('-' * 30)