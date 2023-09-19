# utilização de break com while
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    print(numero)



# utilização de break com for
    for numero in range(100):

        if numero == 10:
            break

        print(numero, end=" ")

# utilização de continue com while
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        continue
    print(numero)



# utilização de continue com for
    for numero in range(100):

        if numero == 10:
            continue

        print(numero, end=" ")
