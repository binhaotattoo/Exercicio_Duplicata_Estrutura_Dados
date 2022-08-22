#IMPLEMENTAR A CLASSE DE VETORES ORDENADOS


import random


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = - 1
        self.valores = self.capacidade*[0]
        
    def imprime(self):
        if self.ultima_posicao == - 1:
            print("o vetor esta vazio")
        else:
            for i in range (self.ultima_posicao + 1):
                print(i, '-', self.valores[i])
    
    def insere(self, valor):
        
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade maxima atingida")
            return
        
        posicao = 0        
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
    
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x = x - 1
            
        self.valores[posicao] = valor
        self.ultima_posicao = self.ultima_posicao + 1
        
    def pesquisa_linear(self,valor):
        operacoes = 0
        for i in range(self.ultima_posicao + 1):
            operacoes += 1
            if self.valores[i] == valor:    
                return i, operacoes
        return - 1, operacoes 
            
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        operacoes = 0
        while True:
            operacoes += 1
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            #se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual, operacoes
            #se não achou
            elif limite_inferior > limite_superior:
                return - 1, operacoes
            #Divide os limites
            else:
                #Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                #Limite superior
                else:
                    limite_superior = posicao_atual - 1
    
    def excluir (self, valor):
        posicao, operacoes = self.pesquisa_linear(valor)
        if posicao == -1:
            return operacoes
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1
        return operacoes                            
                
                
            
                
#==================
#Adicionando testes
#==================

amostragem = [1, 10, 100, 1000]

print("n \t linear\t binario")
for num_elementos in amostragem:
    #num_elementos = 1000
    vetor = VetorOrdenado(num_elementos)
    valores = random.sample(range(0, 2*num_elementos),num_elementos)
    #print(valores)
    
    for valor in valores:
        vetor.insere(valor)
    #vetor.imprime()
    
    interacoes = 5
    operacoes_binaria_media = 0
    operacoes_linear_media = 0
    for i in range(interacoes):
        endereco, operacoes_linear = vetor.pesquisa_linear(random.randrange(0, 2*num_elementos))
        operacoes_linear_media += operacoes_linear
        
        endereco, operacoes_binaria = vetor.pesquisa_binaria(random.randrange(0, 2*num_elementos))
        operacoes_binaria_media += operacoes_binaria
        
    operacoes_linear_media = int(operacoes_linear_media/interacoes)
    operacoes_binaria_media = int(operacoes_binaria_media/interacoes)
    
    print("{}  \t {}  \t  {}".format(num_elementos, operacoes_linear_media, operacoes_binaria_media))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#num_elementos = 100
#vetor = VetorOrdenado(num_elementos)

#valores = random.sample(range(0, 2*num_elementos), num_elementos )
#print(valores)


#for valor in valores:
#    vetor.insere(valor)
#vetor.imprime()

#valor = random.randrange(0, 2*num_elementos )
#posicao, operacoes_linear = vetor.pesquisa_linear(valor)
#posicao, operacoes_binaria = vetor.pesquisa_binaria(valor)

#print("linear \t binario")
#print("{} \t {}".format(operacoes_linear, operacoes_binaria))


