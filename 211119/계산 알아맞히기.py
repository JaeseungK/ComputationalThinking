import random

def make_question():
  # x op y
  x = random.randint(1,40)
  y = random.randint(1,40)

  # 1은 더하기 2는 빼기 3은 곱하기
  op = random.randint(1,3)

  string = ''

  string += str(x)

  if op == 1:
    string += '+'
  elif op == 2:
    string += '-'
  else :
    string += '*'

  string += str(y)

  return string

succes = 0
for i in range(5) :
  string = make_question()
  #stting은 함수이다

  n =int(input(string + '='))
  answer = eval(string)
  #eval() 함수는 안의 수식을 계산해서 반환한다
  
  if n == answer:
    print('정답입니다')
    succes += 1
  else :
    print('오답입니다')

print('맞은 개수 : ', succes)

