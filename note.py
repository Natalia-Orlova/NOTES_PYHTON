import csv
from datetime import datetime as dt
from menu import main_menu

def add_note():
    time = dt.now().strftime('%D %H:%M')
    head = input('Введите заголовок заметки: ')
    note = input('Введите тело заметки: ')
    with open('notes.csv', 'a', encoding='cp1251') as myFile:
        myFile.write('{}; {}; {}\n'
                    .format(head, note, time))

# def show_notes_list():
#     with open('notes.csv', 'r', encoding='cp1251') as file:
#         read_file = file.read()
#     print(read_file)

def show_notes_list():
    with open('notes.csv', 'r', encoding='cp1251') as file:
        data_reader = csv.reader(file)
        for index, line in enumerate(data_reader):
            print(index, *line)

def edit_note():
    with open('notes.csv', 'r') as file:
        lines = file.readlines()
    c = input('Выберите номер заметки для редактирования или нажмите "q" для выхода в меню: \n')
    if c == 'q':
        main_menu()
    else:
        try:
            print(lines[int(c)])
            a = input('введите слово или строку, которую хотите заменить: ')
            b = input('введите новое слово или строку: ')
            lines[int(c)] = lines[int(c)].replace(a, b)
            print('Изменения успешно сохранены\n')
        except IndexError:
            print('Заметки с таким номером нет, повторите попытку!\n')
        except ValueError:
            print('Некорректный ввод! Необходимо ввести цифру.')
        with open('notes.csv', 'w') as file:
            file.writelines(lines)
    
def remove_note():
    with open('notes.csv', 'r') as file:
        lines = file.readlines()
    c = input('\nВыберите номер заметки для удаления или нажмите "q" для выхода в меню: ')  
    if c == 'q':
        main_menu()  
    else: 
        try:
            del lines[int(c)]
            print(f'\nЗаметка под номером {c} успешно удалена!\n')
        except IndexError:
            print('Заметки с таким номером нет, повторите попытку!\n')
        except ValueError:
            print('Некорректный ввод! Необходимо ввести цифру.')
        with open('notes.csv', 'w') as file:
            file.writelines(lines)
