#정의
def print_menu():
  print('1.치즈버거 세트')
  print('2.불고기버거 세트')
  print('3.치킨버거 세트')
  print('4.종료')

menu = {1:'치즈버거 세트', 2:'불고기버거 세트', 3:'치킨버거 세트', 4:'종료'}

def check_menu(x):
  if x in menu:
    print(menu.get(x),'가 선택되었습니다.')
  else:
    print('잘못된 메뉴를 선택하셨습니다.')

#실행
print_menu()

x = int(input('메뉴 번호를 선택하세요 : '))

check_menu(x)

