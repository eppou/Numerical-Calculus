import numpy as np


def funcao(x):
    return x**3+ 6*x**2 + 12*x - 11

def derivada(x):
    return 3*x**2 + 12*x + 12

def newton_raphson(f, df, x0, tol=1e-6, maxiter=100):
    """
    Implementação do método de Newton-Raphson para encontrar a raiz de uma função.

    Argumentos:
    f -- a função para a qual queremos encontrar a raiz.
    df -- a derivada da função f.
    x0 -- o valor inicial da iteração.
    tol -- a tolerância (default = 1e-6).
    maxiter -- o número máximo de iterações (default = 100).

    Retorna:
    x -- a raiz da função f.
    """
    x = x0
    for i in range(maxiter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x = x - fx / dfx
    return x

a = 0
b = 1
tol = 1e-6
maxiter = 40
x0 = -1

raiz = newton_raphson(funcao,derivada,x0,tol,maxiter)

print("A raiz aproximada é: ",raiz)