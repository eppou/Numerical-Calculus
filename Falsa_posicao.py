import numpy as np

def funcao(x):
    return x**3+ 6*x**2 + 12*x - 11


def falsa_posicao(funcao, a, b, tol, iter_max):
    fa = funcao(a)
    fb = funcao(b)
    iteracao = 0

    while iteracao < iter_max:
        iteracao += 1
        c = (a * fb - b * fa) / (fb - fa)
        fc = funcao(c)

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c

a = 0
b = 1
tol = 1e-6
maxiter = 40

raiz = falsa_posicao(funcao,a,b,tol,maxiter)

print("A raiz aproximada é: ",raiz)
