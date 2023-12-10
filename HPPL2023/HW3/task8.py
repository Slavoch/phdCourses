from mpi4py import MPI
import time
import sys
import cupy
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

time0 = time.time()

if sys.argv[2] =="cupy":
    engine = cupy
elif sys.argv[2] =="numpy":
    engine = np

def get_evolution_matrix(N_iter, rs, xs,engine):
    """
    From r_list,x_list, make tensor M_i = M[r_j,x_k,time_i]
    and make evolution of whole matrix as M_i = rs * M_(i-1) * (1-M_(i-1))
    return tensor M_i = M[r_j,x_k,time_i]
    """
    mat = engine.zeros((xs.shape[0], rs.shape[0], N_iter)) # float by default
    mat[:, :, 0] = engine.meshgrid(rs, xs)[1]
    for t in range(1, N_iter):
        mat[:, :, t] = rs * mat[:, :, t - 1] * (1 - mat[:, :, t - 1])
    if engine ==cupy:
        mat = cupy.asnumpy(mat)
    return mat

def get_last_m(mat, m, n):
    """
    From tensor M take elements from time_n to time_(n + m)

    """
    return mat[:, :, n : n + m]

N_iter = 100
resolution = int(sys.argv[1])

if engine == cupy:
    rs_total = cupy.linspace(0, 4, resolution) # float by default
    xs = cupy.linspace(0.001, 1, resolution,endpoint=False) # float by default
else:
    rs_total = np.linspace(0, 4, resolution) # float by default
    xs = np.linspace(0.001, 1, resolution,endpoint=False) # float by default


r_step = (resolution//size)

if rank == size-1:
    rs =rs_total[r_step * rank:]
else:
    rs = rs_total[r_step * rank:r_step * (rank+1)]


mat = get_evolution_matrix(N_iter, rs, xs,engine)

m = 10
last_mat = get_last_m(mat, m, N_iter - m)
last_mat = (last_mat * xs.shape[0]).astype(int)
img = np.zeros((last_mat.shape[0], last_mat.shape[1]), dtype=np.int64) + 1
for t in range(m):
    for i,col in enumerate(last_mat[:, :, t].T):
        converged_rows, counts = np.unique(col, return_counts=True)
        img[converged_rows,i] += counts

amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
fh_result = MPI.File.Open(comm,f"./img_proc_{size}_res{resolution}_{sys.argv[2]}.txt", amode)
offset =  comm.Get_rank() * resolution * r_step * 8
fh_result.Write_at_all(offset, img.T.flatten())

fh_timer = MPI.File.Open(comm, f"./time_proc_{size}_res{resolution}_{sys.argv[2]}.txt", amode)

offset =  comm.Get_rank() * 4
timer = np.array([time.time() - time0],dtype= np.float32)
fh_timer.Write_at_all(offset, timer)

MPI.Finalize()
