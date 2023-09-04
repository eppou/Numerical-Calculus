import math

import numpy as np


def isTridiagonal(m):
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if ((i == j) or (i - 1 == j) or (i + 1 == j)):
                if (m[i][j] == 0):
                    return False
            else:
                if (m[i][j] != 0):
                    return False

    return True

def isDD(m):

    for i in range(0,len(m)):
        n1 = 0
        n2 = 0
        for j in range(0,len(m)):
            if(i == j):
                n1 = m[i][j]
            else:
                n2 = n2 + math.fabs(m[i][j])
        if(n1 < n2):
            return False
    return True


def tridiagonal_vectors(A):
    """
    Extrai os vetores a, b e c de uma matriz tridiagonal A.

    Parâmetros:
        A (numpy array): Matriz tridiagonal de dimensão (n, n).

    Retorno:
        a (numpy array): Vetor diagonal inferior de A.
        b (numpy array): Vetor diagonal principal de A.
        c (numpy array): Vetor diagonal superior de A.
    """
    n = A.shape[0]
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)

    for i in range(n):
        b[i] = A[i,i]
        if i > 0:
            a[i] = A[i,i-1]
            c[i-1] = A[i-1,i]

    return a, b, c


def thomas_algorithm(a, b, c, d):
    n = len(d)
    c_dash = np.zeros(n-1)
    d_dash = np.zeros(n)
    x = np.zeros(n)

    # Modifying the coefficients
    c_dash[0] = c[0] / b[0]
    d_dash[0] = d[0] / b[0]

    for i in range(1, n-1):
        c_dash[i] = c[i] / (b[i] - a[i] * c_dash[i-1])

    for i in range(1, n):
        d_dash[i] = (d[i] - a[i] * d_dash[i-1]) / (b[i] - a[i] * c_dash[i-1])

    # Back substitution
    x[n-1] = d_dash[n-1]
    for i in range(n-2, -1, -1):
        x[i] = round(d_dash[i] - c_dash[i] * x[i+1],1)

    return x


#---------------MAIN------------------#

A = np.array([[2, 1, 0, 0, 0],
              [1, 2, 1, 0, 0],
              [0, 1, 2, 1, 0],
              [0, 0, 1, 2, 1],
              [0, 0, 0, 1, 2]], dtype='double')

if not isTridiagonal(A):
    raise ValueError("A matriz deve ser Tridiagonal para o algoritmo ser eficiente")

if not isDD(A):
    raise ValueError("A matriz deve ser Diagonalmente Dominante")

B = np.array([4, 4, 0, 0, 2], dtype='double')

a,b,c = tridiagonal_vectors(A)
d = B

print("O vetor a é: \n",a)
print("O vetor b é: \n",b)
print("O vetor c é: \n",c)
print("O vetor d é: \n",d)

X = thomas_algorithm(a,b,c,d)

print("Vetor Solução: \n",X)

