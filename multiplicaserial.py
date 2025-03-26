import numpy as np
import time

# Tamanho da matiz
N = 1000

# Arquivos
f1 = f"data/matrix_A_{N}.csv"
f2 = f"data/matrix_B_{N}.csv"
fr = f"data/matrix_Resutado_{N}.csv"

# Carregar as matrizes salvas
A = np.loadtxt(f1, delimiter=",", dtype=np.int32)
B = np.loadtxt(f2, delimiter=",", dtype=np.int32)

# Obter o tamanho da matriz
N = A.shape[0]

# Inicializar a matriz resultado com zeros
C = np.zeros((N, N), dtype=np.int32)

# Medir tempo de execução
start_time = time.time()

# Multiplicação sequencial de matrizes
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i, j] += A[i, k] * B[k, j]

# Tempo total de execução
end_time = time.time()
execution_time = end_time - start_time

# Salvar a matriz resultante para conferência
np.savetxt(fr, C, delimiter=",", fmt="%d")

print(f"Multiplicação sequencial concluída em {execution_time:.2f} segundos.")
