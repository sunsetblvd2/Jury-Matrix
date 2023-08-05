import numpy as np
import sys
import pdb

r_N = 3 # 2n - 3
c_N = 4 # n + 1

start_col_offset = 1
jury_mat = np.zeros((r_N,c_N))
for i in range(0, r_N):
    
    if i > 1: 
        print('Initialization done. Check jury matrix.')
        pdb.set_trace()
    
    start_col = c_N - start_col_offset
    print(start_col)
    for j in range(0, c_N):

        if i == 0 or i == 1: # initialization
            
            if i % 2 == 0:  # even row
        
                jury_mat[i, j] = float(sys.argv[j + 1])
        
            else:
        
                jury_mat[i, j] = float(sys.argv[c_N - j])

            

        else:
    
            if i % 2 == 0:

                if start_col > 0:

                    det_mat = np.zeros((2, 2))
                    
                    det_mat[0, 0] = jury_mat[i - 2, 0]
                    det_mat[1, 0] = jury_mat[i - 1, 0]
                    det_mat[0, 1] = jury_mat[i - 2, start_col]
                    det_mat[1, 1] = jury_mat[i - 1, start_col]

                    print(det_mat)

                    pdb.set_trace()

                    jury_mat[i, j] = np.linalg.det(det_mat)
                    if i < r_N - 1:
                        jury_mat[i+1] = np.roll(np.flip(jury_mat[i]), -start_col_offset)
                    start_col -= 1

    if i % 2 == 0:

        if i > 1:

            start_col_offset += 1

print(jury_mat)
pdb.set_trace()
