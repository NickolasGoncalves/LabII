
def menu():
    print("## MERCADINHO DO SEU ZÉ ##")
    print("1- Adicionar um produto: ")
    print("2- Buscar um produto: ")
    print("3- Vizualizar todos os produtos: ")
    print("4- Vender um produto: ")
    print("5- Relatório de vendas: ")
    opc = int(input("O que você deseja? "))
    return opc

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
    for product_name, product_info in my_dict.items():
        amount = product_info["amount"]
        price = product_info["price"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")

def buscar_produto(my_dict):
    busca = input("Digite o nome do Produto: ")
        
    if busca in my_dict:
        print(f"Procurando {busca}...")
        for product_name, product_info in my_dict.items():
            amount = product_info["amount"]
            price = product_info["price"]
            print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")
    else:
        print(f"Produto {busca} não registrado")

def produto_estoque(my_dict):
    for product_name, product_info in my_dict.items():
        amount = product_info["amount"]
        price = product_info["price"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")

def venda_produto(my_dict):
    product_name = input("Digite o nome do produto vendido: ")
    quantity_sold = int(input("Digite a quantidade vendida: "))

    if product_name in my_dict:
        product = my_dict[product_name]
        current_quantity = product['amount']
        
        if quantity_sold <= current_quantity:
            product['amount'] -= quantity_sold
            sale_value = quantity_sold * product['price']
            print(f"Venda realizada com sucesso! Valor total: R$ {sale_value}")
        else:
            print("Quantidade em estoque insuficiente.")
    else:
        print("Produto não encontrado no estoque.")


        
def main():
    my_dict= {}
    
    while True:
        opc = menu()
        if opc == 1:
            while True:
                adicionar_produto(my_dict)
                if input("Deseja adicionar outro produto? (s/n): ").lower() != "s":
                    break
        elif opc == 2:
            buscar_produto(my_dict)
        elif opc == 3:
            produto_estoque(my_dict)
        elif opc == 4:
            while True:
                venda_produto(my_dict)
                if input("Deseja comprar outro produto? (s/n): ").lower() != "s":
                    break

        
    
  



main()
