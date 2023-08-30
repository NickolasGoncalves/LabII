29/08
def count_numbers(my_list):
    count_dict = {}
    for number in my_list:
        #count_dict[number] = count_dict.get(number, 0) + 1
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
def main():
    my_list = [1, 2, 3, 4, 5, 4, 3]
    
    result = count_numbers(my_list)
    
    print(f"Resultado: {result}")
main()
