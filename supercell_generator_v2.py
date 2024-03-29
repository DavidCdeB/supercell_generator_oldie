#

import numpy as np
import itertools
import sys
import pdb
from itertools import product

# Direct matrix lattice vectors (primitive cell):
# Aragonite:
A =np.array([[0.496160000000e+01,   0.000000000000e+00 ,  0.000000000000e+00],
             [0.000000000000e+00,   0.797050000000e+01,   0.000000000000e+00],
             [0.000000000000e+00,   0.000000000000e+00,   0.573940000000e+01]])

# Direct matrix lattice vectors (primitive cell):
# Calcite I:
#A =np.array([[   0.288155519353E+01,   0.000000000000E+00,   0.568733333333E+01],
#             [  -0.144077759676E+01,   0.249550000000E+01,   0.568733333333E+01],
#             [  -0.144077759676E+01,  -0.249550000000E+01,   0.568733333333E+01]])

# Supercell expansion matrix generator:
# Calcite I:
K = 3
N = 3
E = [np.reshape(np.array(i), (K, N)) for i in itertools.product([0, 2], repeat = K*N)]

# Supercell expansion matrix generator:
# Aragonite:
K = 3
N = 3
E = [np.reshape(np.array(i), (K, N)) for i in itertools.product([0, 1, -1], repeat = K*N)]


tol_1 = 10
tol_2 = 1E-8

print 'type(E) = ', type(E) # Each E candidate is saved in a list
#print 'E = ', E            # If you want to check all possible combinations.
print 'len(E) = ', len(E)   # No. combinations = (#integers)**9 

for indx_E in E:
#     print 'type(indx_E) = ', type(indx_E) # They're already a <numpy.ndarray>
#     indx_E = np.asarray(indx_E)  # Each indx_E is already a <numpy.ndarray>; there is no need to convert. 
      A_SC = np.dot(indx_E,A)
      a1_SC = np.linalg.norm(A_SC[0])
      a2_SC = np.linalg.norm(A_SC[1])
      a3_SC = np.linalg.norm(A_SC[2])

      det_indx_E = np.linalg.det(indx_E)

#     If you want to print each iteration, uncomment this block:
#     print 'a1_SC = ', a1_SC
#     print 'a2_SC = ', a2_SC
#     print 'a3_SC = ', a3_SC
#     print 'det_indx_E = ', det_indx_E

#     print  abs(a1_SC - a2_SC) == tol_2  # All False, thus we have to use <=
#     print  abs(a1_SC - a2_SC) <= tol_2

      if  a1_SC > tol_1\
          and a2_SC > tol_1\
          and a3_SC > tol_1\
          and abs(a1_SC - a2_SC) <= tol_2\
          and abs(a1_SC - a3_SC) <= tol_2\
          and abs(a2_SC - a3_SC) <= tol_2\
          and det_indx_E > 0.0:
             print 'A_SC = ', A_SC

             print 'a1_SC = ', a1_SC
             print 'a2_SC = ', a2_SC
             print 'a3_SC = ', a3_SC
             print 'det_indx_E = ', det_indx_E 
             E_sol = np.dot(A_SC, np.linalg.inv(A))
             print 'E_sol = ', E_sol
             print 'END ++++++++++' 
#              

