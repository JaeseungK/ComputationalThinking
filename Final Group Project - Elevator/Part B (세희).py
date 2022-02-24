# A

import random

ev1_floor = random.randint(1,46)
ev2_floor = random.randint(1,46)
ev3_floor = random.randint(1,46)

floor = [ev1_floor, ev2_floor, ev3_floor]

ev_stance = ['up', 'down', 'stay']

ev1_stance = random.choice(ev_stance)
ev2_stance = random.choice(ev_stance)
ev3_stance = random.choice(ev_stance)

stance = [ev1_stance, ev2_stance, ev3_stance]


# B

# 1층이거나 46층일때 운행상태 수정
# 운행상태에 따른 목적지 정하기

ev1 = {ev1_floor:ev1_stance}
ev2 = {ev2_floor:ev2_stance}
ev3 = {ev3_floor:ev3_stance}

while True :
    if (ev1_floor == 1 and ev1_stance == 'down') or (ev1_floor == 46 and ev1_stance == 'up') :
        ev1_stance == random.choice(ev_stance)
    elif (ev2_floor == 1 and ev2_stance == 'down') or (ev2_floor == 46 and ev2_stance == 'up') :
        ev2_stance = random.choice(ev_stance)
    elif (ev3_floor == 1 and ev3_stance == 'down') or (ev3_floor == 46 and ev3_stance == 'up') :
        ev3_stance = random.choice(ev_stance)
    else :
        break

print("각 엘리베이터 현재위치 =", floor)
print("각 엘리베이터 이동상태 =", stance)

arriv = ['', '', '']

for i in range(3) :
    if stance[i] == 'up' :
        arriv[i] = random.randint(floor[i]+1,46)
    elif stance[i] == 'down' :
        arriv[i] = random.randint(1,floor[i]-1)
    else :
        arriv[i] = floor[i]

print("엘리베이터 목적지 =", arriv)

