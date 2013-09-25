from __future__ import division
import math
def linapprox(function,a,b,gridpoints,x):
	gridlength = (b-a)/(gridpoints-1)
	grid = [i*gridlength for i in range(gridpoints)]
	fpoints = [function(i) for i in grid]
#	print zip(grid, fpoints)
	
	for index,xi in enumerate(grid):
		if xi > x: break
	slope = (fpoints[index] - fpoints[index -1])/gridlength
	return fpoints[index-1]+(x-grid[index-1])*slope
	
print linapprox(math.sqrt,0,1,50,0.5)

#check solution
def linapprox2(f, a, b, n, x):
    """
    Evaluates the piecewise linear interpolant of f at x on the interval 
    [a, b], with n evenly spaced grid points.

    Parameters 
    ===========
        f : function
            The function to approximate

        x, a, b : scalars (floats or integers) 
            Evaluation point and endpoints, with a <= x <= b

        n : integer
            Number of grid points

    Returns
    =========
        A float. The interpolant evaluated at x

    """
    length_of_interval = b - a
    num_subintervals = n - 1
    step = length_of_interval / num_subintervals  

    # === find first grid point larger than x === #
    point = a
    while point <= x:
        point += step

    # === x must lie between the gridpoints (point - step) and point === #
    u, v = point - step, point  

    return f(u) + (x - u) * (f(v) - f(u)) / (v - u)
    
print linapprox2(math.sqrt,0,1,50,0.5)