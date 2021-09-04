#import requests
import pymorphy2

# читаем с компа
pf = open( r'c:\Downloads\text.txt', 'tr', encoding='utf-8')
f = pf.read()
pf.close(  )

# Убрать знаки препинания (все что мешает словам)
l = lambda x : ' ' if x in ',.;?!-—«»\n' else x
f2 = "".join(  l(c) for c in f  )
f2 = ' '.join( f2.split() )   # убрать двойные пробелы
#print( f2 )


# Список
lst = f2.split( ' ' )
print(lst)

# нижний регистр
lst = list(  map( str.lower, lst )  )
print( lst )

# Л Е М М А Т И З А Ц И Я
lst_m=[]
morph = pymorphy2.MorphAnalyzer()
for word in lst:
    p = morph.parse( word )[0]
    lst_m.append( p.normal_form )
print('Лемматизация:\n', lst_m )

# уникальные слова
lstUnique = list(  set( lst_m )  )
print( 'всего слов=', len(lst), 'Уникальных слов=',len( lstUnique )  )

# словарь частотности слов
dic = {}
s = str( lst_m)
for word in lstUnique:
    n = s.count( word )
    dic[word] = n
print( 'словарь частотности слов\n',dic )

#Сортировка по частоте
ds = sorted(  dic.items(), key=lambda x: x[1], reverse=True )
#print( ds )
print( '5 наиболее часто встречающихся слов:\n',ds[:5])
print( 'Уникальных слов=',len( lstUnique )  )



