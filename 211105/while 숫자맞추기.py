ans = 50
cnt = 0
x = int(input('숫자룰 맞춰보세요 :'))
while cnt < 5 :
 cnt = cnt+1
 if x == ans :
   print('정답입니다 !')
 elif x > ans :
    print('정답은 더 작은 숫자입니다')
 else :
   print('정답은 더 큰 숫자입니다')
 x = int(input('숫자룰 다시 맞춰보세요 :'))
