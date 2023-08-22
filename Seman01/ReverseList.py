#Passo 1: Criar uma função de reversão, primeiro preciso de um espaço para salvar minha lista.
#Passo 2: Criação de um '(for)' para percorrer a minha lista, tendo como ponto de referencia o ultimo indice da lista.
#Passo 3: Criar uma Variavel que adicione os numeros.
#Passo 4: Devolver a ao Main()
def reverse_list(list):
    reverse = []
    for i in range(len(list) - 1, -1, -1):
        reverse.append(list[i])
    return reverse #
#Passo 1: Criar uma lista
#Passo 2: Enviar a Função '(Reverse)'.
#Passo 3: Criar uma Variavel para receber a nova lista;
def main():
    my_list = [1, 2, 3, 4, 5]
    list = reverse_list(my_list)
    print(list)

main()
