# supercell_generator
Given a direct matrix lattice vectors, this program creates supercell candidates for which the lattice parameters are smaller than a chosen value, and the three of them of the same size, within a tolerance.

This allows to construct supercells for different poymorphs with lattice paramenters of equal legth, so that we ensure phonons are calculated within a "sphere" of equal radius


Given the matrices `{aij}`, `{Eij}` and `{aij_SC}`, it is satisfied that:


    #  |a1x a1y  a1z|          |E11 E12  E13|        |a1x_SC a1y_SC  a1z_SC|     
    #  |a2x a2y  a2z|    x     |E21 E22  E23|     =  |a2x_SC a2y_SC  a2z_SC|
    #  |a3x a3y  a3z|          |E31 E32  E33|        |a3x_SC a3y_SC  a3z_SC|
    # \--------------/        \--------------/      \-----------------------/ 
    #   {aij} matrix            {Eij} matrix           {aij_SC} matrix
    #  (i=1,2,3; j=x,y,z)       (i,j=1,2,3)            (i=1,2,3; j=x_SC,y_SC,z_SC) 
    #   Known                   


where `x` stands for a standard matrix multiplication (rows, columns).

**1)** Each element of `{aij}` matrix is known:

``` 
a1x = 0.288155519353E+01
a1y = 0.000000000000E+00
a1z = 0.568733333333E+01
    
a2x = -0.144077759676E+01             # Eqns(1)
a2y = 0.249550000000E+01
a2z = 0.568733333333E+01
    
a3x = -0.144077759676E+01
a3y = -0.249550000000E+01
a3z = 0.568733333333E+01
```

**2)** Each element of `{Eij}` is a list of possible integer values, the same for each element:

```
E11 = [0, 1, 2, -1, -2]
E12 = [0, 1, 2, -1, -2]
E13 = [0, 1, 2, -1, -2]
    
E21 = [0, 1, 2, -1, -2]              
E22 = [0, 1, 2, -1, -2]              # Eqns(2)
E23 = [0, 1, 2, -1, -2]
    
E31 = [0, 1, 2, -1, -2]
E32 = [0, 1, 2, -1, -2]
E33 = [0, 1, 2, -1, -2]
```

**3)** `a1_SC`, `a2_SC` and `a3_SC` are calculated in the following way:

```
a1_SC =  (a1x_SC**2 + a1y_SC**2 + a1z_SC**2)**(0.5)
a2_SC =  (a2x_SC**2 + a2y_SC**2 + a2z_SC**2)**(0.5)    # Eqns(3)
a3_SC =  (a3x_SC**2 + a3y_SC**2 + a3z_SC**2)**(0.5)
```

I would like to brute force loop over all possible `Eij` values (Eqns(2)) so that I can find those `Eij` for which:

[![enter image description here][1]][1]

I have been thinking that a way to implement this eqn (67) is through this function:

    def tolerance(a1_SC, a2_SC, a3_SC):
        tol_1 = 10
        tol_2 = 0.001
        return a1_SC > tol_1\
               and a2_SC > tol_1\
               and a3_SC > tol_1\
               and abs(a1_SC - a2_SC) < tol_2\
               and abs(a1_SC - a3_SC) < tol_2\ 
               and abs(a2_SC - a3_SC) < tol_2

When it comes the time to calculate:

    a1x_SC = E11 * a1x + E12 * a2x + E13 * a3x
    a1y_SC = E11 * a1y + E12 * a2y + E13 * a3y
    a1z_SC = E11 * a1z + E12 * a2z + E13 * a3z
    
    a2x_SC = E21 * a1x + E22 * a2x + E23 * a3x           # Eqns (4)
    a2y_SC = E21 * a1y + E22 * a2y + E23 * a3y
    a2z_SC = E21 * a1z + E22 * a2z + E23 * a3z
    
    a3x_SC = E31 * a1x + E32 * a2x + E33 * a3x
    a3y_SC = E31 * a1y + E32 * a2y + E33 * a3y
    a3z_SC = E31 * a1z + E32 * a2z + E33 * a3z

There is this problem: considering what has been said above, it would be necessary to loop over the 5 possible values of `E11` (`E11 = [0, 1, 2, -1, -2]`), while  `E12`, `E13`, `E21`, `E22`, `E23`, `E31`, `E32` and `E33` remain the same. This means this pseudocode:

    for e11 in E11:
      a1x_SC = e11 * a1x + E12[0] * a2x + E13[0] * a3x
      a1y_SC = e11 * a1y + E12[0] * a2y + E13[0] * a3y
      a1z_SC = e11 * a1z + E12[0] * a2z + E13[0] * a3z
    
      a2x_SC = E21[0] * a1x + E22[0] * a2x + E23[0] * a3x           # Eqns (5)
      a2y_SC = E21[0] * a1y + E22[0] * a2y + E23[0] * a3y
      a2z_SC = E21[0] * a1z + E22[0] * a2z + E23[0] * a3z
    
      a3x_SC = E31[0] * a1x + E32[0] * a2x + E33[0] * a3x
      a3y_SC = E31[0] * a1y + E32[0] * a2y + E33[0] * a3y
      a3z_SC = E31[0] * a1z + E32[0] * a2z + E33[0] * a3z
    
      #####
    
      a1x_SC = e11 * a1x + E12[1] * a2x + E13[1] * a3x
      a1y_SC = e11 * a1y + E12[1] * a2y + E13[1] * a3y
      a1z_SC = e11 * a1z + E12[1] * a2z + E13[1] * a3z
    
      a2x_SC = E21[1] * a1x + E22[1] * a2x + E23[1] * a3x           # Eqns (6)
      a2y_SC = E21[1] * a1y + E22[1] * a2y + E23[1] * a3y
      a2z_SC = E21[1] * a1z + E22[1] * a2z + E23[1] * a3z
    
      a3x_SC = E31[1] * a1x + E32[1] * a2x + E33[1] * a3x
      a3y_SC = E31[1] * a1y + E32[1] * a2y + E33[1] * a3y
      a3z_SC = E31[1] * a1z + E32[1] * a2z + E33[1] * a3z

      .
      .
      .

but this would not be considering all the possible combinations, because for a given `e11`, for instance, it is also valid:

      a1x_SC = e11 * a1x + E12[0] * a2x + E13[0:-1] * a3x

How could achieve this goal? 

The final result would be to save in a file the candidates that satisfy Eq. 67 in this way:

    |E11 E12  E13|  
    |E21 E22  E23|  
    |E31 E32  E33|  
    <Value of `a1_SC`>    <Value of `a2_SC`>    <Value of `a3_SC`>
    
    |E11 E12  E13|  
    |E21 E22  E23|  
    |E31 E32  E33|  
    <Value of `a1_SC`>    <Value of `a2_SC`>    <Value of `a3_SC`>
    .
    .
    .

Code:

    #  |a1x a1y  a1z|    
    #  |a2x a2y  a2z|    
    #  |a3x a3y  a3z|    
    # \--------------/   
    #   {aij} matrix     
    #  (i=1,2,3; j=x,y,z)
    #   Given            

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




  [1]:  https://github.com/DavidCdeB/supercell_generator/blob/master/67.png



