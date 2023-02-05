students = {
    1: {'name':'Davlat','surname': 'Kattabekov','age': 18, 'jinsi': 'erkak', 'mark': 3},
    2:{'name':'Farrux','surname': 'Zohirov','age': 20, 'jinsi': 'erkak', 'mark': 5},
    3:{'name':'Xurshid','surname': 'Boltaboev','age': 19, 'jinsi': 'erkak', 'mark': 3},
    4:{'name':'Muhammadzohir','surname': 'Roziev','age': 23, 'jinsi': 'erkak', 'mark': 4},
    5:{'name':'Doston','surname': 'Davlatov','age': 25, 'jinsi': 'erkak', 'mark': 5},
    6:{'name':'Ergash','surname': 'Ganiev','age': 19, 'jinsi': 'erkak', 'mark': 2},
    7:{'name':'Farida','surname': 'Sayfullaeva','age': 18, 'jinsi': 'ayol', 'mark': 5},
    8:{'name':'Maftuna','surname': 'Abdurahmonova','age': 18, 'jinsi': 'ayol', 'mark': 5},
    9:{'name':'Muslima','surname': 'Latipova','age': 19, 'jinsi': 'ayol', 'mark': 2},
    10:{'name':'Imona','surname': 'Shokirjonova','age': 19, 'jinsi': 'ayol', 'mark': 5,}

}

student_id = int(input('enter student id: '))

if student_id in students:
    mark = students[student_id]['mark']
    if mark == 3:
        print('yomon')
    elif mark == 3:
        print('Yaxshi')
    else:
        print('Alo')
else:
    print('student not found')




















