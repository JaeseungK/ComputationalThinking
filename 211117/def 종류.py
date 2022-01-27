#가능한 함수의 모형은 아래 4가지
#입력값과 반환값의 유무에 따름

def add1():
  a = 10
  b = 20
  print(a + b)

def add2():
  a = 10
  b = 20
  return a+b

def add3(a,b):
  print(a + b)

def add4(a,b):
  sum = a + b
  return sum

#함수호출
add1()

sum = add2()
print(sum)

add3(10,20)

x = 10
y = 20
add3(x,y)

print(add4(x,y))
