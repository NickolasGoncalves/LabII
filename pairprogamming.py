def menu():
    print("1 - Verificar o total de horas trabalhadas e ausentes de um funcionário em questão.")
    print("2 - Alterar o total de horas trabalhadas de um funcionário em questão")
    print("3 - Alterar o total de horas ausentes de um funcionário em questão.")
    print("4 - Mostrar o salário do funcionário.")
    print("5 - Mostrar o código do usuário com seu respectivo total de horas ")
    print("6 - Resetar o vetor ")
    print("7 - Sair ")
    opcao = int(input("Escolha uma Opção: "))
    return opcao
    
def verificar(horas,ausentes):
    f = int(input("Digite a posição do funcionário em questão: "))
    print("A quantidade de horas trabalhadas é: ", horas[f])
    print("A quantidade de horas ausentes é : ", ausentes[f])

def alterar_trabalhada(horas,ausentes):
    f = int(input("Digite a posição do funcionário em questão: "))
    x = int(input("Digite a nova quantidade de horas: "))
    horas[f] = x
    ausentes[f] = 44 - x
    
def alterar_ausente(horas,ausentes):
    f = int(input("Digite a posição do funcionário em questão: "))
    x = int(input("Digite a nova quantidade de horas ausentes: "))
    ausentes[f] = x
    horas[f] = 44 - x
    
def mostrar_salario(horas):
    y = int(input("Digite a posição do funcionário que deseja verificar o salário: "))
    for x in horas:
        salario = horas[y] * 50
    print("O salário do funcionário é: ", salario)

def mostrar_codigo(horas,ausentes):
    posicao = 0
    posicao2 = 0
    for x in horas:
        posicao = posicao + 1
        print(posicao,"-","Horas trabalhadas: ",x)
    for i in ausentes:
        posicao2 = posicao2 + 1
        print(posicao2,"-","Horas ausentes: ",i)
    
def resetar(horas,ausentes):
    horas.clear()
    ausentes.clear()
    for x in range(20):
        horas.append(44)
    for x in range(20):
        ausentes.append(0)

def main():
    ausentes = []
    horas = []
    opcao = 0
    for x in range(20):
        horas.append(44)
    for x in range(20):
        ausentes.append(0)
    while opcao != 7:
        opcao = menu()
    
        if opcao == 1:
            verificar(horas,ausentes)
        
        elif opcao == 2:
            alterar_trabalhada(horas,ausentes)
            
        elif opcao == 3:
            alterar_ausente(horas,ausentes)
            
        elif opcao == 4:
            mostrar_salario(horas)
            
        elif opcao == 5:
            mostrar_codigo(horas,ausentes)
            
        elif opcao == 6:
            resetar(horas,ausentes)
        elif opcao == 7:
            print("Sair!")
 
main()
