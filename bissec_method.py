import numpy as np

def funcao(x):
    return x**3+ 6*x**2 + 12*x - 11

def bissecao(f, a, b, tol=1e-8, maxiter=100):
    """
    Encontra a raiz de uma função f em um intervalo [a, b] usando o método da bissecção.

    Parâmetros:
    f (função): a função contínua cuja raiz deve ser encontrada.
    a (float): o limite inferior do intervalo.
    b (float): o limite superior do intervalo.
    tol (float, opcional): a tolerância para a raiz. O padrão é 1e-8.
    maxiter (int, opcional): o número máximo de iterações permitido. O padrão é 100.

    Retorna:
    float: a raiz da função f.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("Não é possível encontrar a raiz em [a, b]. pois f(a)*f(b) < 0")

    for i in range(maxiter):
        c = (a + b) / 2
        fc = f(c)

        if np.abs(fc) < tol:
            return c

        print("O ponto medio entre A e B é {} e seu f(x) = {} , iteração numero {}\n".format(c, fc, i))

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise ValueError("O método não convergiu após {} iterações.".format(maxiter))

a = 0
b = 1
tol = 1e-6
maxiter = 40

raiz = bissecao(funcao, a, b, tol, maxiter)

print("A raiz aproximada é: ",raiz)

