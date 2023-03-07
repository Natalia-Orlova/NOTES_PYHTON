import csv
from datetime import datetime as dt


# def new_note():
#     head = input('Введите заголовок заметки: ')
#     note = input('Введите тело заметки: ')
#     print(head + '; ' + note)


def add_note():
    time = dt.now().strftime('%D %H:%M')
    head = input('Введите заголовок заметки: ')
    note = input('Введите тело заметки: ')
    with open('notes.csv', 'a', encoding='cp1251') as myFile:
        myFile.write('{}; {}; {}\n'
                    .format(head, note, time))


# def save_note():


def show_notes_list():
    with open('notes.csv', 'r', encoding='cp1251') as file:
        read_file = file.read()
    print(read_file)

# add_note()
# show_notes_list()