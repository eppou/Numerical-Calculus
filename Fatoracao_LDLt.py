import numpy as np


def pivotize(matrix):
    """
    Executa pivoteamento em uma matriz quadrada, retornando a matriz de pivoteamento P
    e a matriz resultante A após a aplicação do pivoteamento.
    """
    # Inicializa a matriz de pivoteamento como uma matriz de identidade
    P = np.identity(matrix.shape[0])

    # Itera sobre as colunas da matriz
    for j in range(matrix.shape[0]):
        # Encontra a linha com o maior elemento em valor absoluto na coluna j
        row = np.argmax(np.abs(matrix[j:, j])) + j

        # Se a linha encontrada for diferente da linha atual, troca as linhas na matriz de pivoteamento e na matriz A
        if row != j:
            P[[j, row], :] = P[[row, j], :]
            matrix[[j, row], :] = matrix[[row, j], :]

    # Retorna a matriz de pivoteamento e a matriz resultante após a aplicação do pivoteamento

    return matrix


def ldl_decomposer(A):
    n = A.shape[0]
    U = np.copy(A)
    L = np.eye(n)

    for i in range(n):
        if (U[i, i] == 0):
            U = pivotize(U)
        p = U[i, i]
        for j in range(i + 1, n):
            mult = U[j, i] / p
            L[j, i] = mult
            U[j] = U[j] - mult * U[i]

    diagonal = np.diag(U)
    D = np.diag(diagonal)
    return L, D


def solve_diagonal(A, b):
    """Resolve um sistema linear com uma matriz diagonal."""
    print(A)

    n = len(b)
    x = np.zeros(n, dtype=A.dtype)
    for i in range(n):
        x[i] = b[i] / A[i, i]
    return x


def solve_triangular(matrix, b, lower=False):
    n = len(matrix)
    x = np.zeros(n)

    if lower:
        for i in range(n):
            s = np.dot(matrix[i, :i], x[:i])
            x[i] = (b[i] - s) / matrix[i, i]
    else:
        for i in range(n - 1, -1, -1):
            s = np.dot(matrix[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - s) / matrix[i, i]

    return x


def ldl_solver(A, b):
    L, D = ldl_decomposer(A)
    z = solve_triangular(L, b, True)
    y = solve_diagonal(D, z)
    x = solve_triangular(L.T, y, False)

    return x

A = np.array([[1, 1, 0],
              [1, 2, -1],
              [0, -1, 3]], dtype='double')

b = np.array([2, 1, 5]).reshape(-1, 1)

X = ldl_solver(A,b)

print("Vetor Solução: \n",X)

fi = len(X)
print(X[fi-1])