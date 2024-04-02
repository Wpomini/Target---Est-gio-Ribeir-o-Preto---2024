"""
Questão 1
Resultado: 91
"""

indice = 13
soma = 0
for k in range(indice):
    soma = soma + k + 1
print(soma)

"""
Questão 2
O numero escolhido foi definido previamente na variavel "n"
"""
t1 = 0 
t2 = 1
n= 12
print('{} -> {}'.format(t1, t2), end='')
cont = 3
seq_fib = [t1, t2]
while cont <= 12:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2 
    t2 = t3
    seq_fib.append(t3)
    cont +=1
  
print()
print('-'*60)
if n in seq_fib:
    print('O numero informado pertence a Sequencia de Fibonacci')
else: 
    print('O numero informado NÃO pertence a Sequencia de Fibonacci')

"""
Questão 3
Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, _9_

b) 2, 4, 8, 16, 32, 64, _128_

c) 0, 1, 4, 9, 16, 25, 36, _49_

d) 4, 16, 36, 64, _100_

e) 1, 1, 2, 3, 5, 8, _13_

f) 2,10, 12, 16, 17, 18, 19, _???_ -> Não sei responder, não encontrei lógica :(
"""

"""
Questão 4
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, 
mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
RESPOSTA: Eu ligo o primeiro interruptor e deixo ele ligado por um tempo, depois desligo o primeiro interruptor e ligo o segundo, vou na primeira sala
          se a lampada estiver quente e desligada, significa que o primeiro interruptor controla aquela lampada, se a lampada estiver ligada, o segundo
          interruptor que controla aquela lampada, se não estiver nem quente e nem ligada, o terceiro interruptor que controla aquela lampada. Depois,
          vou na segunda sala e sigo a mesma logica, se estiver quente e desligada é o primeiro interruptor que controla, se estiver ligada é o segundo 
          interruptor que controla, se estiver desligada é o terceiro interruptor que controla. Fazendo isso, descobrimos os interruptores que controlam
          as lampadas.
"""

# Questão 5

string_original = "Python"
string_invertida = ""

for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]
  
print("String original: ", string_original)
print("String invertida: ", string_invertida)

