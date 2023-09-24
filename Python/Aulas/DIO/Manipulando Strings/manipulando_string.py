# modificando texto
nome = "fEliPE"

print(nome.upper())
print(nome.lower())
print(nome.title())

# excluindo espaços
texto = "  Olá, Mundo!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

# centralização
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(19, "#"))

# junção

print("P-y-t-h-o-n")
print("-".join(menu))
