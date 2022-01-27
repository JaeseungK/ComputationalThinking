# B

def turnred() :
 my_floor = int(input_window.get())

 print("내 위치 =", my_floor)

 t_list = []

 for i in range(3) :
   if stance[i] == 'stay' :
     t = abs(my_floor - floor[i])
   else :
     t = abs(floor[i] - arriv[i]) + abs(my_floor - arriv[i])
     
   t_list.append(t)
 
 print('걸리는 시간 =', t_list)

 for i in range(3) :
   if t_list[i] == min(t_list) :
     target_ev = 'EV' + str(i+1)

 print('가장 빠른 엘레베이터 =', target_ev)

 for i in range(3) :
   if t_list[i] == min(t_list) :
     target_evnum = i

 floor_list[target_evnum].configure(fg='red')
 text_list[target_evnum].configure(fg='red')
 stance_list[target_evnum].configure(fg='red')