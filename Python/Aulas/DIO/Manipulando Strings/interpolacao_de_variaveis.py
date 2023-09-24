nome = "Felipe"
idade = 23
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Felipe", "idade": 23, "saldo": 45.435}

# Old Style usando %s/d/f
print("Nome: %s Idade: %d" % (nome, idade))

# usando .format
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

# usando f"""
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
