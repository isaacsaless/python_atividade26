# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    termo = primeiro + i * razao
    print(f'Termo {i+1}: {termo}')