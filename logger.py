def add():
    fam = input('Введите фамилию нового абонента: ')
    number = input('Введите номер нового абонента: ')
    with open('text.txt', 'a', encoding='utf-8') as base:
        base.write('\n' + fam + ' // ' + number)
    print('Номер телефона доабавлен')