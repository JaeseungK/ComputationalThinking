room = input('방 번호 입력: ') 
arr = [0]*9

for i in room:
    if i == '9':
        arr[6] += 1
    else:
        arr[int(i)] += 1
arr[6] = (arr[6] + 1) // 2
print(max(arr))