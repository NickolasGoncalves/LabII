def menu():
    print("=-=-= Escolha uma Opção =-=-= ")
    print("1. Criar novo contato ")
    print("2. Incluir telefone ")
    print("3. Remover um telefone ")
    print("4. Contato um contato ")
    print("5. Buscar um contato")
    print("6. Listar contatos")
    print("7. Sair")
    option = int(input("Escolha uma Opção: "))
    
    return option
    
def add_contact(contacts, contact_name = None):
    if contact_name:
        name = contact_name
        
    name = input("Digite o nome do contato: ")
    contacts[name] = []
    
    while True:
        phone = input(f"Digite um número para contato {name}: ")
        
        if phone == '':
            break
        
        contacts[name].append(phone)
    
def include_contacts(contacts):
    name = input("Escolha um contato para incluir um novo número: ")
    
    if name in contacts:
        #Incluir um novo Número: 
        phone = input(f"Digite um número para o contato {name}:  ")
        contacts[name].append(phone)
    else:
        include_contact = input(f"O contato {name} ainda não existe. Deseja Inclui-lo ? Y/N")
        
        if include_contact == Y:
            add_contact(contacts, name)
            
        print("Contato Inexistente")
        
        
def main():
    
    contacts = {} 
    while True:
        option = menu()
        if option == 1:
            add_contact(contacts)
        
        elif option == 2:
            include_contacts(contacts)
                
            
        elif option == 7:
            print(f"Contatos{contacts}")
            break
    
    
main()
