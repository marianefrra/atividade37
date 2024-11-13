#lendo 20 idades e armazenando na lista 

idades = []
for i in range (20):
    idade = int(input(f"digite a idade {i + 1}: "))
    idades.append(idade)

#encontrando a maior e a menor idade

maior_idade = max(idades)
menor_idade = min(idades)

#exibindo a maior e a menor idade

print(f"maior idade: {maior_idade}")
print(f"menor idade: {menor_idade}")
