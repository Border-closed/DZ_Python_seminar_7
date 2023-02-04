import data
import massivi
import log


def buttom ():
    modul = data.mode()
    if modul == 'i':
        datat = data.tel_data()
        stroka = massivi.spisok_z(datat)
        f=stroka[0]
        i=stroka[1]
        o=stroka[2]
        t=stroka[3]
        k=stroka[4]
        data.inp(f)
        data.inp(i)
        data.inp(o)
        data.inp(t)
        data.inp(k)
        data.inp('')
        log.logg(stroka)
    elif modul == 'e':
        wyw = data.what_you_want()
        strok = massivi.stroka()
        spis = massivi.spisok(strok)
        if wyw in spis:
            f = massivi.massiv(spis,0)
            i = massivi.massiv(spis,1)
            o = massivi.massiv(spis,2)
            t = massivi.massiv(spis,3)
            k = massivi.massiv(spis,4)
            ind=[]
            for j in range (len(f)):
                if wyw==f[j] or wyw==i[j] or wyw==o[j] or wyw==t[j] or wyw==k[j]:
                    ind.append(j)
            text = []
            for x in range (len(ind)):
                text.append(f[ind[x]])
                text.append(i[ind[x]])
                text.append(o[ind[x]])
                text.append(t[ind[x]])
                text.append(k[ind[x]])
            data.out(text)
        else:
            print('Таких данных в справочнике нет')
        log.logg(wyw)
    else:
        print('Вы ввели не валидное значение. Введите режим работы. Экспорт: e, импорт: i')