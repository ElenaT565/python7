import logger as l
import controller as c

def start():
    action = input('Введите добавить, если хотите добавить нового абонента, или найти, если хотите найти номер имеющегося: ')
    if action == 'добавить':
        l.add()
    elif action == 'найти':
        c.search()
    else:
        print("Такого действия нет. Введите добавить или найти")