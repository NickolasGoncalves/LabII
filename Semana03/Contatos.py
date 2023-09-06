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
        
def delete_contact(contacts):
    name = input("Digite o nome do contato que deseja excluir: ")
    
    if name in contacts:
        contacts.pop[name]
    else:
        print(f"O Contato {name} não existe.")
        
    
    if len(contacts[name]) == 1:
        contacts.pop[name]
        return
    
    if name in contacts:
        print("Telefones: ")
        if index in range(len(contacts[name])):
            print(f" {index} : {contacts[name][index]}")
        remove_index = int(input(" Qual número deseja remover ?"))
        contacts[name].pop(remove_index)
        
    else:
        print(f"Contato {name} Inexistente")
        
def find_contacts(contacts):
    name = input("Digite o nome de Contato: ")
    
    if name in contacts:
        print("Telefones: ")
        
        for phone in contacts:
            print(f" {phone} ")
            
    else:
        print(f"O contato {name} não existe.")
        
def main():
    
    contacts = {} 
    while True:
        option = menu()
        if option == 1:
            add_contact(contacts)
        elif option == 2:
            include_contacts(contacts)
        elif option == 3:
            delete_contact(contacts)
        elif option == 4:
            delete_contact(contacts)
        elif option == 5:
            find_contacts(contacts)
        elif option == 6:
            print(contacts)
        elif option == 7:
            print(f"Tchau!")
            break
    
    
main()
