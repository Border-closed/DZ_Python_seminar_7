def mode ():
    r = input('Введите режим работы. Экспорт: e, импорт: i ')
    return r


def tel_data ():
    data = input('Через запятую введите фамилию, имя, отчество, номер телефона (8**********), вид телефона (личный и т.д.) ')
    return data


def what_you_want ():
    wyw = input('Введите данные для поиска ')
    return wyw


def inp (x):
    with open ('telephone.txt', 'a', encoding='utf-8') as inp_tel:
        inp_tel.write(f'{x} \n')


def out (x):
    with open ('telephone_out.txt', 'w', encoding='utf-8') as out_tel:
        out_tel.write(f'{x} \n')