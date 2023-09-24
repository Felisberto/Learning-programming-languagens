numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

'''for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)'''

# modificando valores
numbers = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numbers]

print(quadrado)

'''for numero in numbers:
    quadrado.append(numero ** 2)'''
