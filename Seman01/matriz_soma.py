#Passo 1: Função para Receber a matriz;
#Passo 2: Variavel para receber o valor somado;
#Passo 3: Criação de um '(for)' para percorrer a matriz e encontrar o Maior Número de cada linha
  #Passo 3.1: Pegar o Maior numero somar na Variavel (Total);

def values(matriz):
    total = 0
    for x in matriz:
        num = max(x)
        total += num
    return total #Passo 4: Retornar a Função Local para Global
#Passo 1: Criar uma Matriz;
#Passo 2: Enviar Matriz a função (Values) local.
#Passo 3: Receber a soma da Matriz;
def main():
    matriz =    [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    total = values(matriz)
    print("Soma Total: {}".format(total))

main()
