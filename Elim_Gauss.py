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


def elim_gauss(A, b):
    # Triangularização
    Ab = np.concatenate((A, b), 1)  # 1 = concatena pela coluna
    n = np.shape(Ab)[0]

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            pivot = Ab[i, i]
            m = Ab[j, i] / pivot
            for k in range(0, n + 1):
                Ab[j, k] = Ab[j, k] - m * Ab[i, k]

    # Retrosubstituição
    X = np.ones(n)
    for i in range(n - 1, -1, -1):
        X[i] = Ab[i, n]
        for j in range(i + 1, n):
            X[i] = X[i] - Ab[i, j] * X[j]
        X[i] = X[i] / Ab[i, i]

    return Ab, X


# Matriz do exemplo que está no slide
A = np.array([[8, -2, 5],
              [4, 8, 5],
              [2, -2, 10]], dtype='double')

b = np.array([-1, 15, -12]).reshape(-1, 1)

A = pivotize(A)

# Matriz do exercício do slide
# A = np.array([[10, 1, -1, 2],
#               [4, 9, -1, 3],
#               [2, -2, 12, 5],
#               [1, -3, 5, 15]], dtype='double')
#
# b = np.array([-33, -8, 11, -11]).reshape(-1, 1)

ab, x = elim_gauss(A, b)

print("Matriz A|b Triangularizada: \n", ab)
print("\nVetor solução:\n", x)