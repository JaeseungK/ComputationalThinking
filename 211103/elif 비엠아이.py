weight = float(input('몸무게 입력(킬로그램) :'))
height = float(input('키 입력(미터) :'))

bmi = weight/(height**2)

if bmi < 18.5 :
  print('당신의 BMI 수치는', bmi,'이며 Underweight 입니다')
elif bmi < 25:
  print('당신의 BMI 수치는', bmi,'이며 healthyweight 입니다')
elif bmi < 30:
  print('당신의 BMI 수치는', bmi,'이며 overweight 입니다')
else:
  print('당신의 BMI 수치는', bmi,'이며 obese 입니다')
