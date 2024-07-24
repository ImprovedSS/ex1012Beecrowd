quantia = float(input())
notas = {
    100: 0,
    50.00: 0,
    20.00: 0,
    10.00: 0,
    5.00: 0,
    2.00: 0
}
moedas = {
    1.00: 0,
    0.50: 0,
    0.25: 0,
    0.10: 0,
    0.05: 0,
    0.01: 0
}
for chave in notas.keys():
    if quantia // chave >= 1:
        notas[chave] = quantia // chave
        quantia -= notas[chave] * chave
for chave in moedas.keys():
    if quantia > 0.000000 and chave == 0.01:
        moedas[chave] = quantia * 100
    elif quantia // chave >= 1:
        moedas[chave] = quantia // chave
        quantia -= moedas[chave] * chave
print("NOTAS:")
for chave, valor in notas.items():
    print(f"{valor:.0f} nota(s) de R$ {chave:.2f}")
print("MOEDAS:")
for chave, valor in moedas.items():
    print(f"{valor:.0f} moeda(s) de R$ {chave:.2f}")
