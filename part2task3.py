
# coding: utf-8

# In[ ]:


'''
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''

lst = [int(i) for i in input().split()]
x = int(input())
pos = 0
pos_lst = []
while pos < len(lst):
    if x in lst:
        for i in lst:
            if int(i) == x:
                pos_lst.append(pos)
            pos+=1
    else:
        pos_lst.append("Отсутствует")
        break
for i in pos_lst:
    print(i, end=" ")
