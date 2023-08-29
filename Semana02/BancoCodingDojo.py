'''
Passo 1: Criar uma função para verificar o valor de saque.
Passo 2: Atribuir contagem de notas.
Passo 3: Receber um valor de saque e finalizar quando chegar a 0.
Passo 4: Retornar ao Main()
'''
def verify_troco(saque):
    contador100 = 0
    contador50 = 0
    contador20 = 0
    contador10 = 0
    while saque >= 100:
        contador100 += 1
        saque -= 100
    while saque >= 50:
        contador50 += 1
        saque -= 50
    while saque >= 20:
        contador20 += 1
        saque -= 20
    while saque >= 10:
        contador10 += 1
        saque -= 10
    return contador100, contador50, contador20, contador10

'''
Passo 1: Criar um Parametro Saque para a função Verificar.
Passo 2: Regra de Saque (Notas: 100, 50, 20, 10) (Usar módulo) 
Passo 3: Receber as variaveis "contador". 
'''
def main():
    saque = float(input("Digite o valor do saque: "))
    if saque % 10 != 0:
        while saque % 10 != 0:
            saque = float(input("Digite o valor do saque: " )) 
            print("Somente ")
    
    contador100, contador50, contador20, contador10 = verify_troco(saque)
    print(f"Valor do saque: R$ {saque}, - Resultado esperado: Entregar {contador100} notas de R$100,00. {contador50} notas de R$50,00. {contador20} notas de R$20,00. {contador10} notas de R$10,00" ) 



main()
