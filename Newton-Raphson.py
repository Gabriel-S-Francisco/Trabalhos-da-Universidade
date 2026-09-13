def newton_raphson(a,b,c,d,x0):
    x = x0
    contador = 0
    r = abs (a*x**3 + b*x**2 + c*x + d)
    while r >= 10**(-10) and contador < 1000:
        derivada = 3*a*x**2 + 2*b*x + c
        if derivada == 0:
            break
        x -= (a*x**3 + b*x**2 + c*x + d) / derivada
        r = abs(a*x**3 + b*x**2 + c*x + d)
        contador += 1
    return x,r,contador
raiz,residuo,iteracoes = newton_raphson(float (input ('valor de a: ')),float(input('valor de b: ')),float(input('valor de c: ')),float(input('valor de d: ')),float(input('Chute inicial: ')))
print (f'O polinômio ax³ + bx² + cx + d = 0 possui como raíz: {round (raiz,12)}, com residuo de {residuo} após {iteracoes} iterações')