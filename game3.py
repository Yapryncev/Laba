"""
Игра- угадай слово
"""

import random

word_list = ['автострада', 'эстокада', 'город', 'университет']
poz = 'да'

def restart():
    choise = input('\nХотите заново сыграть?').lower()
    if choise == poz:
        main()
    elif choise == "давай":
        main()
    else:
        print(' Пока !')
        exit()

def print_users_word(arg):
    #secret_word = random.choice(word_list)
    #users_word = ['*'] * len(secret_word)
    print(''.join(arg))



def main():
    errors_counter = 0
    attempts = 2
    secret_word = random.choice(word_list)
    #print(secret_word)
    users_word = ['*'] * len(secret_word)
    print_users_word(users_word)
    while True:
        letter = input('Введите одну букву: ').lower() #если ввести большую букву, введется строчная (или upper)
        if len(letter) != 1 or not letter.isalpha(): #.isaplha проверяет введенный символ на тип
            continue

        if letter in secret_word:
            for pos, char in enumerate(secret_word): # enumerate - пронумировать
            #print(pos, char)
                if letter == char:
                    users_word[pos] = letter
            if '*' not in users_word: # условие выйграша
                print('Вы выйграли')
                print('\tбыло загадано слово:', secret_word)  # \t это табуляция, n и r это новые строки
                break
        else:
            errors_counter += 1
        # errors_counter = errors_counter + 1
            print('\tошибок допущено', errors_counter)
            print('\tОсталось попыток', attempts - errors_counter) #вычисления числа ост. попыток

            if errors_counter == attempts:
                print('Вы проиграли')
                restart()
                break

        print_users_word(users_word)


if __name__ == '__main__':
    main()
