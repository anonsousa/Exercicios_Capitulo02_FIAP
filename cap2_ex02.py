##### QUANTIDADE DE VIAJANTES E DESCONTOS #####


valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))
categoria = int(input("Por favor, informe a categoria:\n 1 - Economica\n 2 - Executiva\n 3 - Primeira Classe"))
quantidade_viajantes = int(input("Por favor, informe a quantidade de viajantes"))

desconto = 0

if categoria == 1:
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.05
elif categoria == 2:
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.08
elif categoria == 3:
    if quantidade_viajantes == 2:
        desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
        desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        desconto = valor_bruto * 0.2
else:
    print("Categoria inexistente, desconto nao concedido")


valor_liquido = valor_bruto - desconto
media_viajantes = valor_liquido / quantidade_viajantes


print(f"O valor da viagem e de {valor_bruto}. Apos os descontos de {desconto}, a viagem custara {valor_liquido}. Cada passageiro tem um custo medio de {media_viajantes}.")

