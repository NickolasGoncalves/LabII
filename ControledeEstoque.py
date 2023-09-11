def add_produto(estoque, nome_produto = None):

    if nome_produto:
        produto = produto_name
        
    produto = input("Nome do Produto: ")

    estoque[produto] = []
    

    while True:
        print("Para finalizar digite '0': ")
        quantidade = int(input(f"Digite a quantidade {produto}: "))
        if quantidade <= 0:
            break
        
        else: 
            valor = float(input(f"Digite valor do {produto}: "))
          
        estoque[produto].append(quantidade)
        estoque[produto].append(valor)

        return 


        



def main():

    estoque = {}

    add_produto(estoque)
    print(add_produto(estoque))


main()
