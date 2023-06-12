# Escrever um programa que receba do teclado um preço e retorne uma parcela de doze do valor indicado, com duas casas decimais de arredondamento

preco = float(input())

parcela = preco/12

print("%.2f" % (parcela))