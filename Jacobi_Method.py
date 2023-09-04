import numpy as np


def Diagonal_notNull_Checker(M):
    n = M.shape[0]
    for i in range(n):
        if (M[i, i] == 0):
            return False

    return True


def Jacobi_Method(A, b, ite):
    n = A.shape[0]
    tol = 0.000001
    x = np.zeros(n)
    x0 = np.zeros(n)
    k = 1
    flag = 0

    while flag == 0:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s = s - A[i, j] * x0[j]

            s += b[i]
            x[i] = s / A[i, i]

            if np.abs(x[i] - x0[i] / x[i]) < tol:
                flag = 1
        x0 = x
        k = k + 1

        if k == ite:
            flag = 1

    return x

A = np.array([[10, 5, -2],
              [3, 12, 4],
              [-5, -6, 15]], dtype='double')

B = np.array([13, 19, 4,], dtype='double')

ite = 100

if not Diagonal_notNull_Checker(A):
    raise ValueError("A matriz deve ter todos os elementos da diagonal não nulos")

X = Jacobi_Method(A,B,ite)

print("Vetor Solução: \n",X)

