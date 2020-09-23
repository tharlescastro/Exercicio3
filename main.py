from Pilha import Pilha

Pilha = Pilha()
menu = '''
---------------
    MENU         		
1 - Adicionar
2 - Remover
3 - Imprmir    
4 - Sair
---------------
Escolha: '''

while True:
    digito = (input(menu))

    if digito == '1':
       	Pilha.addpilha(input('Digite um valor: '))
    elif digito == '2':
        Pilha.remover()   
    elif digito == '3':
        Pilha.imprimirpilha()
    elif digito == '4':
        print("Concluído")1
        break    
    else:
        print('Tente novamente')