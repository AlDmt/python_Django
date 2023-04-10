lst=input('Введите текст ')
lst=lst.split() #разбиваю текст на строки (по слову) 


dup = {x for x in lst if lst.count(x) > 1}
d=' '
dp=d.join(dup)
print('Самое часто встречающее слово (слова): ', dp)

print( 'Самое длинное слово: ', max(lst, key=len)) #самое длинное слово в тексте 
