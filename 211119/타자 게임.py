import random
import time

izone = ['장원영','안유진','권은비','김채원','강혜원','조유리','이채연','사쿠라','나코','히토미','최예나','김민주']

a = random.choice(izone)
 
for i in range(5) :
 

  t1 = time.time()
  print('단어 : ', a)
  b = input('단어를 따라 쳐 보세요 : ')

  if a == b :
    t2 = time.time()
    print('답어 입력까지 걸린 시간 : ', format(t2-t1, '.2f'))
    a = random.choice(izone)
  else :
    print('잘못 입력했습니다')