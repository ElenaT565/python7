import view as v

def main():
    answer = input('Введите да, чтобы начать, или нет, чтобы закончить: ')
    if answer == 'да':
        v.start()
        return(main())
    else:
        print('До свидания!')

main()