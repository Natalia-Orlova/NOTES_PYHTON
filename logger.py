from datetime import datetime as dt
from time import time
from note import add_note

def logger(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}\n'
                    .format(time, data))
        
        