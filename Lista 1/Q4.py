# Faça um programa que leia duas variáveis e retorne o valor de 'H' a partir de uma fórmula

d = float(input())
b = float(input())

h = ((d**2) + 8)/(((d**3) + b)**(1/2))

print("H = %.3f" % h)