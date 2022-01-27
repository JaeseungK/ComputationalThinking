fee = int(input("주머니 사용료는?"))

times = int(input("한 번 두드리면 불어나는 돈의 배수는?")) 
hit = int(input("방망이를 치려는 횟수는?"))

desired = int(input("필요한 돈은 얼마?"))

for i in range(hit, 0, -1):
  seed = (int)((desired + fee) / times)
  desired = seed

print("처음에 넣어야 할 돈: ", seed)