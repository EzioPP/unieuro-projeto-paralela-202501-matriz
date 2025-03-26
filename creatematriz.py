import numpy as np

# Definir tamanho das matrizes
N = 1000

# Gerar duas matrizes aleatórias de tamanho 10000 x 10000 com valores entre 1 e 10
A = np.random.randint(1, 11, size=(N, N), dtype=np.int32)
B = np.random.randint(1, 11, size=(N, N), dtype=np.int32)

# Arquivos
f1 = f"data/matrix_A_{N}.csv"
f2 = f"data/matrix_B_{N}.csv"

# Salvar as matrizes como arquivos CSV
np.savetxt(f1, A, delimiter=",", fmt="%d")
np.savetxt(f2, B, delimiter=",", fmt="%d")

print(f"Matrizes geradas e salvas em {f1} e {f2}")
