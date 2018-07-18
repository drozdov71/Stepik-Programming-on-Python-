
# coding: utf-8

# In[ ]:


'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов 
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
matrix = []
while True:
    n = str(input())
    if n == 'end':
        break
    matrix.append([int(s) for s in n.split()])
out_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        st = len(matrix)
        stlb = len(matrix[0])
        out_matrix[i][j]=int(matrix[i-1][j]) + int(matrix[(i+1)%st][j]) + int(matrix[i][j-1]) + int(matrix[i][(j+1)%stlb])
for i in range(len(out_matrix)):
    for j in range(len(out_matrix[i])):
        print(out_matrix[i][j],end = ' ')
    print()

