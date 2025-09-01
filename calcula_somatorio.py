# lê o valor de n
n = int(input("Digite o valor de n: "))
soma = 0
# laço de 2 até n (inclusive)
for i in range(2, n + 1):
    soma = soma + (i / (i - 1))
print("O valor do somatório é:", soma)
# calcula o somatório de 2/(2-1) + 3/(3-1) + ... + n/(n-1)
# e imprime o resultado