numero_digitado = int(input("Digite um número inteiro: "))

soma = 0

for i in range(1, numero_digitado + 1):
    soma += i

print(f"A soma dos números de 1 até {numero_digitado} é: {soma}")