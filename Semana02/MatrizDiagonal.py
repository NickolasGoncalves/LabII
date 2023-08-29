'''
Passo 1: Criar uma Função para somar a Matriz
Passo 2: Criar uma Variavel para armazenar a soma dos números abaixo da Diagonal Principal
Passo 3: Criar uma Variavel para receber o tamanho da Matriz 
Passo 4: Criar um laço de repetição (Linhas da nossa Matriz)
Passo 5: Criar um laço de repetição (Colunas da Nossa Matriz)
Passo 6: Retornar a soma para o Main()
'''
def sumvalues(matriz):
    total = 0
    tam = len(matriz)
    for x in range(0, tam):
        #print(x, tam) Verificar tamanho
        for z in range(x):
            print(z, x)
            total += matriz[x][z]
            
    return total
'''
Passo 1: Criar Nossa Matriz
passo 2: Enviar a nossa Função sumvalues
'''
def main():
    matriz = [
        [5, 1, 1], # [0,0 0,1 0,2]
        [10, 5, 1], # [1,0 1,1 1,2] (Pengando o 1,0)
        [10, 10, 5] # [0,2 1,2 2,2] (Pegando 2,0 / 2,1 )
    ]

    resultado = sumvalues(matriz)
    print(resultado)

main()
