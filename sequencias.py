# a) 1, 3, 5, 7, ___
a = [1, 3, 5, 7]
a_next = a[-1] + 2
print(f"Próximo número na sequência a) é {a_next}")

# b) 2, 4, 8, 16, 32, 64, ____
b = [2, 4, 8, 16, 32, 64]
b_next = b[-1] * 2
print(f"Próximo número na sequência b) é {b_next}")

# c) 0, 1, 4, 9, 16, 25, 36, ____
c = [0, 1, 4, 9, 16, 25, 36]
c_next = len(c)**2
print(f"Próximo número na sequência c) é {c_next}")

# d) 4, 16, 36, 64, ____
d = [4, 16, 36, 64]
d_next = (len(d) + 2)**2
print(f"Próximo número na sequência d) é {d_next}")

# e) 1, 1, 2, 3, 5, 8, ____
e = [1, 1, 2, 3, 5, 8]
e_next = e[-1] + e[-2]
print(f"Próximo número na sequência e) é {e_next}")

# f) 2,10, 12, 16, 17, 18, 19, ____
# A sequência lógica aqui é a posição da letra 'd' no nome dos números em português
f = [2, 10, 12, 16, 17, 18, 19]
f_next = 200
print(f"Próximo número na sequência f) é {f_next}")
