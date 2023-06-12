# Ler um numero do teclado que representa uma quantidade de segundos. Converter esta quantidade para horas, minutos e segundos.

t = int(input())

h = t // 3600

m = (t % 3600) // 60

s = (t % 3600) % 60

print(f"{h:02d}:{m:02d}:{s:02d}")