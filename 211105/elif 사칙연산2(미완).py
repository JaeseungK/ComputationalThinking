n1 = int(input('fill number1 : '))
n2 = int(input('fill number2 : '))
cal = int(input('fill caculation : '))

if cal != ('+' or '-' or '/' or '*') :
   print('you entered invalid caculation')

if cal == + :
print(n1, cal, n2, '=', n1+n2)
elif cal == - :
  print(n1, cal, n2, '=', n1-n2)
elif cal == * :
  print(n1, cal, n2, '=', n1*n2)
elif cal == / :
  print(n1, cal, n2, '=', n1/n2)
else : 
  print(n1, cal, n2, '=', n1+n2)
