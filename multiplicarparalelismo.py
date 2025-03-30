import numpy as np
import cupy as cp
import psutil as ps
import time
import multiprocessing as mp
from latex import generate_latex_table
N = 10000
CORES = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 3584]

RESULTS = []

f1 = f"data/matrix_A_{N}.csv"
f2 = f"data/matrix_B_{N}.csv"
fr = f"data/matrix_Resutado_{N}.csv"

def multiply_row(args):
    A_row, B, row_index = args
    result_row = []
    for j in range(B.shape[1]):
        result_row.append(np.dot(A_row, B[:, j]))
    return (row_index, result_row)

def matrix_multiply(A, B, x):
    C = np.zeros((A.shape[0], B.shape[1]))
    pool = mp.Pool(processes=x)
    args = [(A[i, :], B, i) for i in range(A.shape[0])]
    results = pool.map(multiply_row, args)
    for row_index, result_row in results:
        C[row_index, :] = result_row
    return C


def matrix_multiply_cuda(A, B):
    A_gpu = cp.array(A)
    B_gpu = cp.array(B)
    C_gpu = cp.matmul(A_gpu, B_gpu)
    return cp.asnumpy(C_gpu)

def main():
    A = np.loadtxt(f1, delimiter=",", dtype=np.int32)
    B = np.loadtxt(f2, delimiter=",", dtype=np.int32)


    for x in CORES:
        start_time = time.time()
        if x == 1:
            C = matrix_multiply(A, B, x)

        elif x == 3584:
            C = matrix_multiply_cuda(A, B)
        else:
            C = matrix_multiply(A, B, x)
        end_time = time.time()
        execution_time = end_time - start_time
        np.savetxt(fr, C, delimiter=",", fmt="%d")
        print(f"Multiplicação usando {x} cores concluída em {execution_time:.2f} segundos.")
        RESULTS.append((x, execution_time))
    generate_latex_table(RESULTS, CPU_MODEL, GPU_MODEL, CPU_COUNT, CPU_PHYSICAL_COUNT, MEMORY)


        
if __name__ == '__main__':
    main()
