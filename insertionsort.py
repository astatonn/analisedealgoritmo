import timeit
import random

x=100
inicio = timeit.default_timer()
A = [] 
A = random.sample (range(5000),x)
print ('######################################')
print ('VETOR ANTES DA ORDENAÇÃO')
print ('######################################')
print (A)
for i in range(1,len(A)): #LAÇO EXTERNO QUE VAI DA POSIÇÃO 1 ATÉ O TAMANHO FINAL DO VETOR
    k = A[i] # CHAVE PARA COMPARAR O ATUAL ELEMENTO
    j = i-1 # J SEMPRE VAI ATUAR COMO COMPARADOR
    while j >= 0 and A[j]>k: # A CONDIÇÃO DE PARADA EH QUANDO O J CHEGA NA PRIMEIRA POSIÇÃO OU SEJA, J VAI PEGAR A POSIÇÃO ATUAL E VAI COMPARANDO ATÉ A PRIMEIRA POSIÇÃO DO VETOR
        # COMPARAÇÃO ENQUANTO MEU TERMO CHAVE FOR MENOR QUE O MEU TERMO ATUAL
        A[j+1] = A[j]  
        j -= 1
    A[j+1] = k

fim = timeit.default_timer()
print ('######################################')
print ('VETOR DEPOIS DA ORDENAÇÃO')
print ('######################################')
print ('duracao: %f' % (fim - inicio))   
print (A)
