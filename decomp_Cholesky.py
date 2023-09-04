import numpy as np


def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i, k] * L[j, k] for k in range(j))
            if i == j:
                L[i, j] = np.sqrt(max(A[i, i] - s, 0))
            else:
                L[i, j] = (1.0 / L[j, j]) * (A[i, j] - s)

    print("Matriz L triangular inferior obtida da Matriz A : \n", L)
    print("Matriz L transposta : \n", L.T)
    return L

def solve_triangular(matrix, b, lower=False):

    n = len(matrix)
    x = np.zeros(n)

    if lower:
        for i in range(n):
            s = np.dot(matrix[i,:i], x[:i])
            x[i] = (b[i] - s) / matrix[i,i]
    else:
        for i in range(n-1, -1, -1):
            s = np.dot(matrix[i,i+1:], x[i+1:])
            x[i] = (b[i] - s) / matrix[i,i]

    return x


def cholesky_solver(A, b):
    # Verifica se a matriz A é simétrica
    if not np.allclose(A, A.T):
        raise ValueError("A matriz deve ser simétrica")

    # Obtém a matriz triangular inferior L da decomposição de Cholesky
    L = cholesky(A)

    # Resolve o sistema triangular inferior L y = b
    y = solve_triangular(L, b, True)

    # Resolve o sistema triangular superior L.T x = y
    x = solve_triangular(L.T, y,False)

    # Retorna o vetor x como solução do sistema linear
    return x

#---------------MAIN------------#
A = np.array([[1, 1, 0],
              [1, 2, -1],
              [0, -1, 3]], dtype='double')

b = np.array([2, 1, 5]).reshape(-1, 1)

X = cholesky_solver(A,b)

print("Vetor Solução: \n",X)

