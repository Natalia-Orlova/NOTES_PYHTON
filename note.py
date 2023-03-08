import csv
from datetime import datetime as dt

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
            print(index, line)

def edit_note():
    print('Выберите номер заметки для редактирования: ')
    show_notes_list()
    
def remove_note():
    with open('notes.csv', 'r') as file:
        lines = file.readlines()
    try:
        c = int(input('\nВыберите номер заметки для удаления: '))
        del lines[c]
        print(f'\nЗаметка под номером {c} успешно удалена!\n')
    except IndexError:
        print('Заметки с таким номером нет, повторите попытку!\n')
    except ValueError:
        print('Некорректный ввод! Необходимо ввести цифру.')
    with open('notes.csv', 'w') as file:
        file.writelines(lines)
    

# add_note()
# show_notes_list()