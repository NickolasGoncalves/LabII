def menu():
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Credito")
    print("4 - Sair! ")
    option = int(input("Escolha uma opção"))
    return option
def deposit(balance):
    money = float(input("Digite o valor de deposito"))
    total = (money + balance)
    return total

def get_the_drift(balance):
    money = float(input("Digite o valor de saque: "))
    total = (money - balance)
    return total

def credit(balance):
    if balance > 0:
        print("Parabéns, você conseguiu os credito!")
    else:
        print("Você está negativado, lamentamos o ocorrido.")

def main():
    bank = balance = float(input("Digite valor em caixa: "))
    opc = menu()
    

    while opc <= 4:
        if option == 1:
            deposit()
        elif option == 2:
            get_the_drift()
        elif option == 3:
            credit()
        elif option == 4:
            print("Você saiu! Até a proxima.")
            break
        else:
            print("Digite um valor valido.")



main()
