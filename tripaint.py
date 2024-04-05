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

def f_shading(img, vertices, vcolors):
    """
    Performs a triangle shading with the average color of its vertices and returns
    the input image with the triangle rendered on top.
    """

    ret_img = np.copy(img)
    triangle_color = np.average(vcolors,0)

    sides = np.array([
        [0,1],
        [1,2],
        [2,0],
    ])

    sides_x = vertices[:,0][sides]
    sides_y = vertices[:,1][sides]
    s_ind = np.argsort(sides_y,1)
    sides_y_sorted = np.take_along_axis(sides_y,s_ind,1)
    sides_x_sorted = np.take_along_axis(sides_x,s_ind,1)
    sides_ymin = sides_y_sorted[:,0]
    sides_ymax = sides_y_sorted[:,1]
    sides_xmin = sides_x_sorted[:,0]
    ymin = np.min(sides_ymin)
    ymax = np.max(sides_ymax)

    dx = vertices[:,0][sides[:,1]] - vertices[:,0][sides[:,0]]
    dy = vertices[:,1][sides[:,1]] - vertices[:,1][sides[:,0]]
    invm = dx/dy

    if np.isnan(invm).any():
        print(f"got isnan:\n{vertices}")
        print(f"skipping")
        return ret_img

    horizontal_sides = np.isinf(invm)
    non_horizontal_sides = np.logical_not(horizontal_sides)

    #find active sides for ymin
    active_sides = np.array([False,False,False])
    new_active_sides = (sides_ymin == ymin)
    active_sides = np.logical_or(active_sides,new_active_sides)
    active_sides = np.logical_and(active_sides,non_horizontal_sides)

    border_points_x = sides_xmin.astype(np.float64)
    rounded_border_points_x = np.round(border_points_x).astype(np.int32)

    for y in range(ymin,ymax+1):
        active_rounded_border_points_x = rounded_border_points_x[active_sides]
        sorted_arbp = np.sort(active_rounded_border_points_x)
        for x in range(int(sorted_arbp[0]), int(sorted_arbp[-1])+1):
            ret_img[x,y] = triangle_color

        new_active_sides = (sides_ymin == y+1)
        removed_active_sides = (sides_ymax == y)
        unchanged_active_sides = np.logical_and(active_sides, np.logical_not(removed_active_sides))
        active_sides = np.logical_or(unchanged_active_sides,new_active_sides)
        border_points_x[unchanged_active_sides]+=invm[unchanged_active_sides]
        rounded_border_points_x = np.round(border_points_x).astype(np.int32)

    return ret_img