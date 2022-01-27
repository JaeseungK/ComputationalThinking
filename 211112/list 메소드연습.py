idle = ['전소연', '송우기', '서수진']

print('(0) ',idle)

idle.append('조미연')
print('(1) ',idle)

idx = idle.index('송우기') 
idle.insert(idx, '송우기') 
print("(2) ", idle)

x = idle.count('송우기')
print('(3) ', x)

idle.remove('서수진')
print('(4) ',idle)

del(idle[1])
print('(5) ',idle)

idle.sort(reverse = True)
print('(6) ',idle)