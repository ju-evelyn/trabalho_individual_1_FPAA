def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    n = max(len(str(num1)), len(str(num2)))
    m = n // 2

    parte1num1, parte2num1 = divmod(num1, 10 ** m)
    parte1num2, parte2num2 = divmod(num2, 10 ** m)

    # Recursividade (divisão)
    rec1 = karatsuba(parte1num1, parte1num2)
    rec2 = karatsuba(parte2num1, parte2num2)
    rec3 = karatsuba((parte2num1 + parte1num1), (parte2num2 + parte1num2))

    # Combinação (conquista)
    return (rec1 * 10**(2*m)) + ((rec3 - rec1 - rec2) * 10**m) + rec2

# Teste
num11 = 1234
num22 = 5678
result = karatsuba(num11, num22)
print(f"{num11} * {num22} = {result}")
