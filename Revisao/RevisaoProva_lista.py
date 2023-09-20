my_list = [8 ,6 ,9 ,4 ,2 ,3 ,5 ,7 , 1]
'''
for index_one in range(len(my_list)):
  min_index = index_one
  
  for index_two in range(index_one, len(my_list)):
    if my_list[index_two] < my_list[min_index]
    min_index = index_two


min_value = my_list[min_index]
my_list[min_index] = my_list[index_one]
my_list[index_one] = min_value
'''
'''
for index in range(len(my_list):              
  for index_one in range(len(my_list)):
    if (index_one + 1) < len(my_list) and my_list[index_one] > my_list[index_one + 1]
    tmp = my_list[index_one]
    my_list[index_one] = my_list[index + 1]
  
print(my_list)
'''

matriz = [
    [8 ,6 ,9] ,
    [4 ,2 ,3] ,
    [5 ,7 , 1]
]



for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        min_line = line
        min_column = column

        for line_aux in range(line, len(matriz)):
            start = column if line == line_aux else 0
            
            for column_aux in range(start, len(matriz[line_aux])):
                if matriz[line_aux][column_aux] < matriz[min_line][min_column]:
                    min_line = line_aux
                    min_column = column_aux
            
        min_value = matriz[min_line][min_column]
        matriz[min_line][min_column] = matriz[line][column]
        matriz[line][column] = min_value

print(matriz)
            
            


