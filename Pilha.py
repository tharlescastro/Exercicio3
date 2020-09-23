from No import No


class Pilha:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def verificavazio(self):
        if self.tamanho == 0:
            return True
        return False

    def addpilha(self, valor):
        no = No(valor)
        if self.verificavazio():
            self.primeiro = no
        else:
            aux = self.primeiro
            self.primeiro = no
            no.proximo = aux
        self.tamanho += 1

    def imprimirpilha(self):
        if self.verificavazio():
            print('Pilha vazia')
        else:
            aux = self.primeiro
            while (aux):
                print(str(aux.dado))
                aux = aux.proximo

    def remover(self):
        if self.verificavazio(): 
            print('Pilha vazia')
        else:
            aux = self.primeiro.proximo
            self.primeiro = aux
            self.tamanho -= 1
        '''
            print("A pilha após exclusão: ")
            imprimirpilha(self)
        '''



