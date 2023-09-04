import  numpy as np

def funcao(x):
    return x**3+ 6*x**2 + 12*x - 11


def secant_method(f, x0, x1, tol=1e-6, maxiter=100):
    """
    Implementação do método das secantes para encontrar a raiz de uma função.

    Argumentos:
    f -- a função para a qual queremos encontrar a raiz.
    x0 -- o primeiro valor inicial da iteração.
    x1 -- o segundo valor inicial da iteração.
    tol -- a tolerância (default = 1e-6).
    maxiter -- o número máximo de iterações (default = 100).

    Retorna:
    x -- a raiz da função f.
    """
    for i in range(maxiter):
        fx0 = f(x0)
        fx1 = f(x1)
        x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x - x1) < tol:
            return x
        x0, x1 = x1, x
    return x


a = 0
b = 1
tol = 1e-6
maxiter = 40
x0 = -1
x1 = 0

raiz = secant_method(funcao,x0,x1,tol,maxiter)

print("A raiz aproximada é: ",raiz)