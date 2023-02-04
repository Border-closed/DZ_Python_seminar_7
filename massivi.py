# считывание файла в строку
def stroka ():
    with open ('telephone.txt', 'r', encoding='utf-8') as str_tel:
        line=str_tel.read()
    return line


# деление строки в список
def spisok (stroka):
    spis_tel=stroka.split()
    return spis_tel


# деление строки в список по запятой
def spisok_z (stroka):
    spis_tel=stroka.split(',')
    return spis_tel


# деление списка на списки фио/тел/вид
def massiv (spisok, x):
    m=[spisok[i] for i in range(x,len(spisok),5)]
    return m
