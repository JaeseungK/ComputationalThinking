car = ['Gene', 'Lex', 'Infini', 'Lambor', 'Linc']

print('현재 차종 : ', car)

car.append('Merce')
print('Merce 차종 추가: ', car)

car.remove('Lex')
print('Lex 차종 단종: ', car)

car.append('Gene-2019')
print('Gene 2019년형 추가: ', car)

print('두 번째부터 네 번째 개발한 모델: ', car[1:4])
