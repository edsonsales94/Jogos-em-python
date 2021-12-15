
idade = [21,28,35,42]

def ano_q_vem(idade):
  return idade+1

valor = [ano_q_vem(idade) for idade in idade if idade > 30]
print(valor)


