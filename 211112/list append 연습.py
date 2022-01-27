datalist = [] 
total = 0

for i in range(5):
  indata = int(input("Enter 5 integers: "))
  datalist.append(indata)
  total = total + indata
print(datalist) 
avg = total / 5 
print("평균:", avg)