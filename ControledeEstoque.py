def adicionar_produto(my_dict):
    product_name = input("Digite o nome do produto (ou deixe vazio para sair): ")
    
    if product_name == '':
        return
    
    product_amount = int(input("Digite a quantidade do produto: "))
    product_price = float(input("Digite o preço do produto: "))

    my_dict[product_name] = {
      "amount": product_amount,
      "price": product_price
    }

def main():
    my_dict= {}
    
    while True:
        adicionar_produto(my_dict)
        
       
        if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
            break
    
  



main()
