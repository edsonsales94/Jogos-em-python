idade=[15,45,66,75,32,11,34]
print(list(range(len(idade))))
print(list(reversed(idade)))
print(list(enumerate(idade)))

print(sorted(idade, reverse=True))
for indice, idade in enumerate(idade):
    print(indice , '-' , idade)


usuario = [
    ("GUILHERME", 37, 1981),
    ("DANIELA", 31, 1987),
    ("PAULO", 39,1979)
]
for nome, _, nasc in usuario:
    print(nome,',', nasc)