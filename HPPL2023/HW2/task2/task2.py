from mpi4py import MPI
from numpy import pi, exp, fft
import numpy as np
import time as  timer
import sys
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
time0 = timer.time()

A,B,N = np.array(sys.argv[1:4],dtype=int)


intervals = np.linspace(A, B, size + 1)
for i in range(size):
    interval = intervals[rank : rank + 2]

if rank == size -1:
    N = N // size + N % size
else:
    N = N // size

    
# def take_integral(f, interval,N):
#     A,B =interval
#     x = np.linspace(A, B, N + 1)
#     y = f(x)
#     y_right = y[1:]
#     y_left = y[:-1]
#     dx = (B - A) / N
#     integral = dx * np.sum(y_right + y_left) / 2
#     return integral

def take_integral(f, interval,N):
    A,B =interval
    x = np.linspace(A, B, N + 1)
    dx = (B - A) / N 
    y = f(x)
    cum_sum = 0
    for n in range(N):
        cum_sum += y[n+1] + y[n]
    return cum_sum * (dx/2)
        



# print(interval,N)
integral = take_integral(np.exp,interval,N)
integral_list = comm.gather(integral, root=0)

if rank ==0:
    print(sum(integral_list),timer.time()- time0)


MPI.Finalize()
