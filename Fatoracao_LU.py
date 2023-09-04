import numpy as np

#-------------------verifica se é triangular inferior-------------------------#
def isInferior(m):
    for i in range(0, len(m)):
        for j in range(i + 1, len(m)):
            if(m[i][j] != 0):
                    return False
    return True

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

def lu_solve(A):
    n=A.shape[0]
    U=np.copy(A)
    L=np.eye(n)
    for i in range(n):
        if(U[i,i] == 0):
            U =pivotize(U)
        p = U[i,i]
        for j in range(i+1,n):
            mult = U[j,i]/p
            L[j,i]= mult
            U[j]= U[j]-mult*U[i]

    return  L,U

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


A = np.array([[8, -2, 5],
              [4, 8, 5],
              [2, -2, 10]], dtype='double')

b = np.array([-1, 15, -12]).reshape(-1, 1)

L,U = lu_solve(A)

y = solve_triangular(L,b,True)

x = solve_triangular(U,y,False)

print("\nVetor solução:\n", x)