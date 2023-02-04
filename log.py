import datetime

def logg(stroka):
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{stroka}, время запроса {str(datetime.datetime.now())} \n')