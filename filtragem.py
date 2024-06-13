# Lista de tuplas contendo ano e valor de vendas
vendas = [
    ('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), 
    ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), 
    ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), 
    ('2022', 5616)
]

# Filtrando valores de vendas para o ano de 2022 onde o valor de vendas é maior que 6000
filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]

# Imprimindo a lista filtrada
print(filtro)
