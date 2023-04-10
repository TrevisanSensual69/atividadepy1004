numero = int(input("Digite um número no formato CDU: "))
c = numero // 100
du = numero % 100
d = du // 10
u = du % 10
print(f"Centena={c}\nDezena={d}\nUnidade={u}")

