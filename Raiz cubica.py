from math import sqrt
def raiz_cubica(a,b,c,d):
    delta0 = b**2 - 3 *a*c
    delta1 = 2 * (b**3) - 9*a*b*c + 27*(a**2)*d
    delta = (delta1 ** 2) - 4 * (delta0**3) 
    if delta > 0:
        raiz_delta = sqrt (delta)
        flag = False
    elif delta == 0:
        raiz_delta = 0
        flag = True
    else:
        raiz_delta = complex (0,sqrt(abs(delta)))
        flag = True
    parcial_soma = ((delta1 + raiz_delta)/2)
    parcial_subtrai = ((delta1 - raiz_delta)/2)
    C = parcial_soma ** (1/3)
    if abs(C) < 1e-14:
        C = parcial_subtrai**(1/3)
    if abs(delta0) < 1e-14 and abs(delta1) < 1e-14:
        x1 = x2 = x3 =  (-1/(3*a)) * (b + C)
    elif flag:
        C2 = C * (-1 + complex(0, sqrt(3))) / 2
        C3 = C * (-1 - complex(0, sqrt(3))) / 2

        x1 = (-1 / (3 * a)) * (b + C + delta0 / C)
        x2 = (-1 / (3 * a)) * (b + C2 + delta0 / C2)
        x3 = (-1 / (3 * a)) * (b + C3 + delta0 / C3)
        x1 = x1.real
        x2 = x2.real
        x3 = x3.real
    else:
        x1 = (-1/(3*a)) * (b + C + (delta0/C)).real
        C2 = C * (-1 + complex (0,sqrt(3)))/2
        n = (-1/(3*a)) * (b + C2 + (delta0/C2))
        x2 = n.real
        x3 = abs(n.imag)
    return x1, x2, x3, flag

import matplotlib.pyplot as plt
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))       
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))


x1, x2, x3, flag = raiz_cubica(a, b, c, d)
if flag:
    print (f'As raízes são reais: {x1}; {x2}; e {x3}')
else:
    print (f'O polinômio possui raízes complexas: {x1}; {x2} + {x3}i; e {x2} - {x3}i')
if flag:
    menor_raiz = x1
    maior_raiz = x1

    if x2 < menor_raiz:
        menor_raiz = x2
    if x3 < menor_raiz:
        menor_raiz = x3

    if x2 > maior_raiz:
        maior_raiz = x2
    if x3 > maior_raiz:
        maior_raiz = x3
else:
    menor_raiz = x1
    maior_raiz = x1

largura = maior_raiz - menor_raiz

if largura == 0:
    largura = 1

xmin = menor_raiz - 0.5 * largura
xmax = maior_raiz + 0.5 * largura

quantidade_pontos = 500
passo = (xmax - xmin) / (quantidade_pontos - 1)

x_anterior = xmin
y_anterior = (
    a*x_anterior**3
    + b*x_anterior**2
    + c*x_anterior
    + d
)

for indice in range(1, quantidade_pontos):
    x_atual = xmin + indice * passo
    y_atual = (
    a*x_atual**3
    + b*x_atual**2
    + c*x_atual
    + d
)

    plt.plot(
        (x_anterior, x_atual),
        (y_anterior, y_atual),
        color="blue")

    x_anterior = x_atual
    y_anterior = y_atual

plt.axhline(0, color="black", linewidth=0.8)

if flag:
    plt.scatter(x1, 0, color="red")
    plt.scatter(x2, 0, color="red")
    plt.scatter(x3, 0, color="red")
    plt.title("Polinômio com três raízes reais")
else:
    plt.scatter(x1, 0, color="red")
    plt.title(
        "Polinômio com uma raiz real e duas raízes complexas"
    )

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()