'''
Alterar valor de um Produto: Crie uma opção para alterações de valor de
determinado produto. O novo valor deve refletir somente nas novas vendas. Crie
também um histórico com os valores do produto.
'''
def add_product(stock):
    """Adiconar/Verificar um Produto ao Estoque"""
    product_name = input("Digite o nome do produto: ")
    if product_name == '':
        return
    if product_name in stock:
        temp_quantity = int(input("Digite a quantidade do produto: "))
        stock[product_name]["amount"] += temp_quantity
    else:
        product_amount = int(input("Digite a quantidade do produto: "))
        product_price = float(input("Digite o preço do produto: R$"))
        product_category = input("Digite uma Categoria")
        stock[product_name] = {
            "amount": product_amount,
            "price": product_price,
            "category": product_category}
        
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
        category = product_info["category"]
    print(f"O produto {product_name} foi adicionado com sucesso!")
    print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}, Categoria: {category}")
    return stock

def find_product(stock):
    """Buscar produto no estoque"""
    product_name = input("Digite o nome do Produto: ")
    if product_name in stock:
        print(f"Procurando {product_name}...")
       
        for amount, price in stock[product_name].items():
            amount = stock[product_name]["amount"]
            price = stock[product_name]["price"]
            print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}")
    else:
        print(f"Produto {product_name} não registrado")

def show_stock(stock):
    """Mostrar completamente o estoque"""
    for product_name, product_info in stock.items():
        amount = product_info["amount"]
        price = product_info["price"]
        category = product_info["category"]
        print(f"Produto: {product_name}, Quantidade: {amount}, Preço: {price}, Categoria: {category}")


