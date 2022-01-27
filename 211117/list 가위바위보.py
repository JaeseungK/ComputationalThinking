rsp = ['가위','바위','보']
rsp.append('기권')

for i in range(len(rsp)) :
  print(i,' : ',rsp[i])

rsp.remove('가위')
print(rsp)

rsp.pop
print(rsp)

del(rsp[1])
print(rsp)