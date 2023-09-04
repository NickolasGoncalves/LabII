'''
Passo 1: Criar uma função Media
Passo 2: Atribuir um Dicionário (Keys and Values)
Passo 3: Criar uma Variavel para puxar o parametro
Passo 4: Percorrer o Dicionário para verificar se o nome está na lista
Passo 5: Criar uma estrutura Condicional para verificar a media
Passo 6: Retornar ao Main()
'''
def media(nome):
    nota_final = {
        'Níckolas' : (7 + 7) / 2,
        'Pedro' : (7 + 9) / 2,
        'Gustavo' : (8 + 8) / 2
    }
    
    
    media = nota_final[nome]
    if nome in nota_final:
        if media < 4 and media >= 0:
            print(f"Reprovado! {nome}{nota_final[nome]}")
        elif media < 7 and media >= 4:
            print(f"Recuperação {nome} {nota_final[nome]}") 
        elif media >= 7 and media <= 10:
            (f"Aprovado!{nome} {nota_final[nome]}")
        else:
            print("Nome não Encontrado")
        return nome, media
'''
Passo 1: Criar um Parametro para a Função Media.
Passo 2: Criar um laço de Repetição 
  Passo 2.1: Criar um condição (break)
Passo 3: Chamar minha função Media para o main()

def main():
    while True:
        nome = input("Digite um Nome: ")
        if nome == "":
            print("Você saiu!")
            break
        nome, resultado = media(nome)
        print(nome, resultado)

        
        
    

main()
