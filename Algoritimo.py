entrada = []

while True:
    num = float(input("Digite um número (-1 para sair): "))
    if num == -1:
        break
    entrada.append(num)

n = len(entrada)

for i in range(n):
    menor_indice = i

    for j in range(i + 1, n):
        if entrada[j] < entrada[menor_indice]:
            menor_indice = j  

    entrada[i], entrada[menor_indice] = entrada[menor_indice], entrada[i]

print("Lista ordenada:", entrada)