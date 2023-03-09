import csv
from datetime import datetime as dt
from menu import main_menu

def add_note():
    time = dt.now().strftime('%D %H:%M')
    head = input('Введите заголовок заметки: ')
    note = input('Введите тело заметки: ')
    with open('notes.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                    .format(head.upper(), note.upper(), time))
    
def show_notes_list():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        data_reader = csv.reader(file)
        print('\nМОИ ЗАМЕТКИ\n')
        for index, line in enumerate(data_reader):
            print(index, *line)
            
def edit_note():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    c = input('Выберите номер заметки для её редактирования: ')
    try:
        print(lines[int(c)])
        a = input('введите слово или строку, которую хотите заменить: ')
        b = input('введите новое слово или строку: ')
        lines[int(c)] = lines[int(c)].replace(a.upper(), b.upper())
        print('Изменения успешно сохранены!\n')
    except IndexError:
        print('Заметки с таким номером нет, повторите попытку!\n')
    except ValueError:
        print('Некорректный ввод! Необходимо ввести цифру.')
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.writelines(lines)
    
def remove_note():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    c = input('\nВыберите номер заметки для её удаления: ')  
    try:
        del lines[int(c)]
        print(f'\nЗаметка под номером {c} успешно удалена!\n')
    except IndexError:
        print('Заметки с таким номером нет, повторите попытку!\n')
    except ValueError:
        print('Некорректный ввод! Необходимо ввести цифру.')
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.writelines(lines)