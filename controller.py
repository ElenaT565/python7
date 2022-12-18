def search():
    get = input('Введите фамилию абонента, которого хотите найти: ')
    with open('text.txt', 'r', encoding='utf-8') as base:
        lines = base.readlines()
        A = []
        for line in lines:
            b = list(line.split(' // '))
            A.append(b)
        for i in range (0, len(A)):
            if A[i][0] == get:
                print('Номер телефона абонента ' + get + ': ' + A[i][1]) 