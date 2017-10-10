#  |a1x a1y  a1z|          |E11 E12  E13|        |a1x_SC a1y_SC  a1z_SC|     
#  |a2x a2y  a2z|    x     |E21 E22  E23|     =  |a2x_SC a2y_SC  a2z_SC|
#  |a3x a3y  a3z|          |E31 E32  E33|        |a3x_SC a3y_SC  a3z_SC|
# \--------------/        \--------------/      \-----------------------/ 
#   {aij} matrix            {Eij} matrix           {aij_SC} matrix
#  (i=1,2,3; j=x,y,z)       (i,j=1,2,3)            (i=1,2,3; j=x_SC,y_SC,z_SC) 
#   Known                   


#  |a1x a1y  a1z|    
#  |a2x a2y  a2z|    
#  |a3x a3y  a3z|    
# \--------------/   
#   {aij} matrix     
#  (i=1,2,3; j=x,y,z)
#   Given            

import numpy as np

a1x = 0.288155519353E+01
a1y = 0.000000000000E+00
a1z = 0.568733333333E+01

a2x = -0.144077759676E+01
a2y = 0.249550000000E+01
a2z = 0.568733333333E+01

a3x = -0.144077759676E+01
a3y = -0.249550000000E+01
a3z = 0.568733333333E+01


# |E11 E12  E13|  
# |E21 E22  E23|  
# |E31 E32  E33|  
#\--------------/ 
#  {Eij} matrix   
#  (i,j=1,2,3)    

E11 = [0, 1, 2, -1, -2]
E12 = [0, 1, 2, -1, -2]
E13 = [0, 1, 2, -1, -2]

E21 = [0, 1, 2, -1, -2]
E22 = [0, 1, 2, -1, -2]
E23 = [0, 1, 2, -1, -2]

E31 = [0, 1, 2, -1, -2]
E32 = [0, 1, 2, -1, -2]
E33 = [0, 1, 2, -1, -2]


# |a1x_SC a1y_SC  a1z_SC|     
# |a2x_SC a2y_SC  a2z_SC|
# |a3x_SC a3y_SC  a3z_SC|
#\-----------------------/ 
#   {aij_SC} matrix
#   (i=1,2,3; j=x_SC,y_SC,z_SC) 

a1x_SC = E11 * a1x + E12 * a2x + E13 * a3x
a1y_SC = E11 * a1y + E12 * a2y + E13 * a3y
a1z_SC = E11 * a1z + E12 * a2z + E13 * a3z

a2x_SC = E21 * a1x + E22 * a2x + E23 * a3x
a2y_SC = E21 * a1y + E22 * a2y + E23 * a3y
a2z_SC = E21 * a1z + E22 * a2z + E23 * a3z

a3x_SC = E31 * a1x + E32 * a2x + E33 * a3x
a3y_SC = E31 * a1y + E32 * a2y + E33 * a3y
a3z_SC = E31 * a1z + E32 * a2z + E33 * a3z

a1_SC =  (a1x_SC**2 + a1y_SC**2 + a1z_SC**2)**(0.5)
a2_SC =  (a2x_SC**2 + a2y_SC**2 + a2z_SC**2)**(0.5)
a3_SC =  (a3x_SC**2 + a3y_SC**2 + a3z_SC**2)**(0.5)


def tolerance(a1_SC, a2_SC, a3_SC):
    tol_1 = 10
    tol_2 = 0.001
    return a1_SC > tol_1\
           and a2_SC > tol_1\
           and a3_SC > tol_1\
           and abs(a1_SC - a2_SC) < tol_2\
           and abs(a1_SC - a3_SC) < tol_2\
           and abs(a2_SC - a3_SC) < tol_2

for e11 in E11:
  a1x_SC = e11 * a1x + E12[0] * a2x + E13[0] * a3x
  a1y_SC = e11 * a1y + E12[0] * a2y + E13[0] * a3y
  a1z_SC = e11 * a1z + E12[0] * a2z + E13[0] * a3z

  a2x_SC = E21[0] * a1x + E22[0] * a2x + E23[0] * a3x           
  a2y_SC = E21[0] * a1y + E22[0] * a2y + E23[0] * a3y
  a2z_SC = E21[0] * a1z + E22[0] * a2z + E23[0] * a3z

  a3x_SC = E31[0] * a1x + E32[0] * a2x + E33[0] * a3x
  a3y_SC = E31[0] * a1y + E32[0] * a2y + E33[0] * a3y
  a3z_SC = E31[0] * a1z + E32[0] * a2z + E33[0] * a3z

