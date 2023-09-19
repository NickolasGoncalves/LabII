my_list = [8 ,6 ,9 ,4 ,2 ,3 ,5 ,7 , 1]

for index_one in range(len(my_list)):
  min_index = index_one
  
  for index_two in range(index_one, len(my_list)):
    if my_list[index_two] < my_list[min_index]
    min_index = index_two


min_value = my_list[min_index]
my_list[min_index] = my_list[index_one]
my_list[index_one] = min_value
