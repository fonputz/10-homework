index = 5
#функція для шифрування(отримує букву)
def tochp (a):
  #Перевіряємо чи це не пробіл
  if a == ' ':
    #якщоце пробіл то ми його не змінюємо і повертаємо користувачу
    return ' '
  else:
    #Дізнаємось номер букви за абеткою, яку ми шифруємо
    c_index= ord(a) - ord('a')
    #Дізнамось номер букви який має бути при шифруванні
    new_index = (c_index+index)%26
    #Дізнаємось індекс букви в системі
    new_chr = new_index + ord('a')
    #повертає зашифровану букву
    return chr(new_chr)

#функція для розшифрування
def frchp (a):
  if a == ' ':
    return ' '
  else:
    c_index= ord(a) - ord('a')
    new_index = (c_index-index)%26
    new_chr = new_index + ord('a')
  #повертає зашифровану букву
    return chr(new_chr)

c = ''
c1 = ''
input_text = input("Enter Text\n")
for i in input_text:
  c = c + tochp(i)
for i in c:
  c1 = c1 + frchp(i)
print('Шифрування: ', c)
print('Розшифрування: ',c1)