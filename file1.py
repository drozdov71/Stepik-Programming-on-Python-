
# coding: utf-8

# In[ ]:


'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. 
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, 
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка 
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. 
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, 
надо отправить в качестве ответа на эту задачу. 
'''
def decompress(s):
    result = ''
    for i in range(len(s)):
        if not s[i].isdigit():
            j = i + 1
            cnt = ''
            while s[j].isdigit():
                cnt += s[j]
                if j + 1 < len(s):
                    j += 1
                else:
                    break
            cnt = int(cnt)
            result += s[i] * cnt
    return result


with open('C:/Users/Dmitry/Downloads/dataset_3363_2.txt', 'r') as f:
    compressed_str = f.readline().strip()

s = decompress(compressed_str)
with open('C:/Users/Dmitry/Downloads/dataset_3363_2.txt', 'w') as f:
    f.write(s)
