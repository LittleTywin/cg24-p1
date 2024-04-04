import numpy as np

def vector_interp(p1,p2,V1,V2,coord,dim):
    """
    Calculates and returns vector value V at point p(x,y) using linear interpolation
    between values V1 at p1 and V2 at p2. Interpolation is performed along given
    axis according to dim value (1 for x, 2 for y). Coord value represents the
    interpolation point coordinate along the given interpolation axis.

    Args:
    p1 (numpy.ndarray) : (2,) point 1 (x1,y1)
    p2 (numpy.ndarray) : (2,) point 2 (x2,y2)
    V1 (numpy.ndarray) : (3,) vector value at point 1
    V2 (numpy.ndarray) : (3,) vector value at point 2
    coord (int) : interpolation point coordinate along interpolation axis
    dim (int) : [1,2] dim=1(2), interpolation along x(y)

    Returns:
    V (numpy.ndarray) : (3,) interpolated value
    """

    denominator = p2[dim-1]-p1[dim-1]
    if denominator == 0:
        return (V1+V2)/2
    interpolation_factor = (coord-p1[dim-1])/denominator
    interpolated_value = V1 + interpolation_factor * (V2-V1)
    return interpolated_value
