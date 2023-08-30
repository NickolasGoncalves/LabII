#29/08
def main():
    buy_list = {}
    
    while True:
        product_name = input("Digite o nome do produto: ")
        if product_name == 'exit':
            break
        
        quantity = int(input("Digite a quantidade: "))
        if product_name in buy_list:
            buy_list[product_name] = buy[product_name] + quantity
        else:
            buy_list[product_name] = quantity
        print(buy_list)
        
    for key in buy_list:
        print(f"Produto: {key} / Quantidade: {quantity}")
        
main()


