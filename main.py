#import requests

'''
Скопирован файл c 'https://drive.google.com/open?id=15fBsTB1ZU_BzEw5SJmlOMX2uuyi1xN1-' на локальный диск
( прочитать с интернета не получилось )
Буду признателен, если укажите как
'''

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

# уникальные слова
lstUnique = list(  set( lst )  )
print( 'всего слов=', len(lst), 'Уникальных слов=',len( lstUnique )  )

# словарь частотности слов
dic = {}
s = str( lst)
for word in lstUnique:
    n = s.count( word )
    dic[word] = n
print( 'словарь частотности слов\n',dic )

#Сортировка по частоте
ds = sorted(  dic.items(), key=lambda x: x[1], reverse=True )
#print( ds )
print( '5 наиболее часто встречающихся слов:\n',ds[:5])
print( 'Уникальных слов=',len( lstUnique )  )



