import random

rsp = ['가위', '바위', '보']

# case(com,user)
case = {('가위','가위'): 0,('바위','바위'): 0,('보','보'): 0,('가위','바위'): 1,('바위','보'): 1,('보','가위'): 1,('가위','보'): -1,('바위','가위'): -1,('보','바위'): -1}

win = 0
lose = 0
draw = 0

for i in range(5):
 print(i+1, '번째 승부입니다')
 com = random.choice(rsp)
 user = input('무엇을 내시겠습니까? :')
 occasion = (com, user)

 print('컴퓨터가',com,'을 내었습니다')
 if case[occasion] == 0 :
   print('비겼습니다')
   draw += 1

 elif case[occasion] == 1 :
   print('당신이 승리했습니다')
   win += 1

 elif case[occasion] == -1 :
   print('컴퓨터가 승리했습니다')
   lose += 1

print('이긴 횟수 :', win)
print('비긴 횟수 :', draw)
print('진 횟수 :', lose)