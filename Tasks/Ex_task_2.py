import os

def print_actions():
    print('''Выберите функцию:
    
    1. Добавить контакт
    2. Удалить контакт
    3. Показать список контактов
    4. Изменить номер
    5. Выход
    ''')

def fix_action(action):
    action = action.strip()
    if action.isdigit():
        action = int(action)
    return action

def fix_phone(phone):
    phone = phone.strip()
    if (len(phone) < 10) or (len(phone)) > 12:
        return -1
    if (len(phone) == 11) and ( (phone[0] == '7') or (phone[0] == '8') ):
        phone = phone[1:]
    if (len(phone) == 12) and (phone[:2] == '+7'):
        if not( phone[1:].isdigit() ):
            return -1
    else:
        if not( phone.isdigit() ):
            return -1
        phone = '+7' + phone
    return phone

def do_action(phone_book, action):
    if action == 1:
        name = ( input('Введите название для контакта: ').strip() ).title()
        phone = input('Введите номер телефона: ')
        phone = fix_phone(phone)
        if phone != -1:
            phone_book[name] = phone
            print('Контакт успешно добавлен!')
        else:
            print('Номер телефона введен неправильно!')
    elif action == 2:
        name = ( input('Введите название контакта: ').strip() ).title()
        tmp_v = phone_book.pop(name, 0)
        if tmp_v != 0:
            print('Контакт успешно удален!')
        else:
            print('Такого контакта не существует!')
    elif action == 3:
        if len(phone_book) > 0:
            for name, phone in phone_book.items():
                print(f'{name}: {phone}')
        else:
            print('Контакты отсутствуют!')
    elif action == 4:
        name = ( input('Введите название контакта: ').strip() ).title()
        tmp_v = phone_book.get(name, 0)
        if tmp_v != 0:
            phone = input('Введите номер телефона: ')
            phone = fix_phone(phone)
            phone_book[name] = phone
            print('Контакт успешно изменен!')
        else:
            print('Такого контакта не существует!')
    else:
        print('Такой функции не существует!')
    return phone_book

phone_book = {}
print_actions()
action = input('Введите номер функции: ')
action = fix_action(action)
while action != 5:
    phone_book = do_action(phone_book, action)
    input()
    os.system('cls')
    print_actions()
    action = input('Введите номер функции: ')
    action = fix_action(action)
print(r'Приложение "Телефонная книга" успешно завершила свою работу!')
input()
