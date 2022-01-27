print('사칙연산 계산하기')
print('======메뉴======')
print('1.덧셈')
print('2.뺄셈')
print('3.곱셈')
print('4.나눗셈')
print('===============')

cal = int(input('메뉴 번호 입력 : '))
num1 = int(input('정수 1 입력 : '))
num2 = int(input('정수 2 입력 : '))

if cal == 1 :
  print(num1 + num2)
elif cal == 2 :
  print(num1 - num2)
elif cal == 3 :
  print(num1 * num2)
elif cal == 4 :
  print(num1 / num2)
else :
  print('잘못 입력하셨습니다')