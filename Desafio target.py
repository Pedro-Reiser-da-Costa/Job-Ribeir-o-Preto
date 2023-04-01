INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f'O valor da variavel soma é {SOMA}')


num = 13

fib = [0, 1]

while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(f'O número {num} pertence à sequência de Fibonacci.')
else:
    print(f'O número {num} não pertence à sequência de Fibonacci.')

seq_a = [1, 3, 5, 7, 9]

seq_b = [2, 4, 8, 16, 32, 64, 128]

seq_c = [0, 1, 4, 9, 16, 25, 36, 49]

seq_d = [4, 16, 36, 64, 100]

seq_e = [1, 1, 2, 3, 5, 8, 13]

seq_f = [2, 10, 12, 16, 17, 18, 19, 20]

prox_a = seq_a[-1] + 2
prox_b = seq_b[-1] * 2
prox_c = seq_c[-1] + (len(seq_c) ** 2)
prox_d = seq_d[-1] + (len(seq_d) ** 2)
prox_e = seq_e[-1] + seq_e[-2]
prox_f = max(seq_f) + 1

print("Próximo elemento de cada sequência:")
print(f"Sequência a: {prox_a}")
print(f"Sequência b: {prox_b}")
print(f"Sequência c: {prox_c}")
print(f"Sequência d: {prox_d}")
print(f"Sequência e: {prox_e}")
print(f"Sequência f: {prox_f}")

# Distância total entre as cidades
distancia_total = 100

# Velocidade do carro em km/h
velocidade_carro = 110

# Velocidade do caminhão em km/h
velocidade_caminhao = 80

# Tempo que levam para se encontrarem em horas
tempo = distancia_total / (velocidade_carro + velocidade_caminhao)

# Distância do carro até Ribeirão Preto em km
distancia_carro_rp = velocidade_carro * tempo

# Distância do caminhão até Ribeirão Preto em km
distancia_caminhao_rp = distancia_total - distancia_carro_rp

if distancia_carro_rp < distancia_caminhao_rp:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

string = input("Digite uma string: ")
invertida = ""

for i in range(len(string)-1, -1, -1):
    invertida += string[i]

print("String invertida: ", invertida)
