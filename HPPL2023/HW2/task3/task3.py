from mpi4py import MPI
import numpy as np
import time as  timer
import sys
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
amode = MPI.MODE_WRONLY|MPI.MODE_CREATE

N = int(sys.argv[1])

rows = 5
cols = 10
img = np.array(list(range(0,cols)) * rows).reshape((rows,cols)).astype(np.uint8)
# img = (np.random.random((rows,cols)) * 100).astype(np.uint8)


col_step = cols //size
if rank == size -1:
    col_w = col_step + cols %size
else:
    col_w = col_step

img_share = img[:,col_step * rank : col_step * rank + col_w]

for i in range(1,N):

    id_next = (rank + 1) % size
    id_prev = (rank - 1) % size

    buffer = np.empty(rows,dtype=np.uint8)
    buffer[:] = img_share[:,-1]
    comm.Send([buffer, MPI.UNSIGNED_CHAR],dest =  id_next,tag=0)
    img_share = np.roll(img_share,1)
    comm.Recv([buffer, MPI.UNSIGNED_CHAR],source = id_prev,tag=0)
    img_share[:,0]=buffer
    
    fh = MPI.File.Open(comm, f"./task3_itter{i}.txt", amode)
    offset =  comm.Get_rank() * rows*col_step
    fh.Write_at_all(offset,img_share.T.flatten())
    fh.Close()

MPI.Finalize()
