# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:06:31 2021

@author: GEON YUK
"""

# 수학시험 프로그램
quiz = (['3+2', 5, 3],['5/2의 몫', 2, 5],['10-2', 8 ,3],['10^2*2', 200, 5],['1-(10/4의 나머지)', -1, 5],['2^4', 16, 3], ['4/2', 2, 3])

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz:
    print('문제 : ', item[0])
    answer = int(input('정답을 입력하세요.'))
    
    if answer == item[1]:
        answerCount += 1
        totalScore += item[2]
    else:
        wrongAnswerCount += 1
        
print('-'*30)
print('정답 개수\t: ', answerCount)
print('오답 개수\t: ', wrongAnswerCount)
print('Total Score\t:', totalScore)
print('-'*30)

# 회원가입 프로그램
members = {}
flag = True

while flag:
    selectNum = int(input('\n1. 회원가입, 2. 프로그램 종료\t'))
    
    if selectNum == 1:
        id = input('아이디를 입력하세요.\t')
        pw = input('비밀번호를 입력하세요.\t')
        members[id] = pw
        
    elif selectNum == 2:
        print('-' * 30)
        print('아이디 : 비밀번호')
        print('-' * 30)
        
        for key in members.keys():
            print(key, '\t:\t', members[key])
        print('-' * 30)
        
        flag = False