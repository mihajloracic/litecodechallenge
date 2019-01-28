import math


def dot(a, b):
    x, y = a
    X, Y = b
    return x * X + y * Y


def length(a):
    x, y = a
    return math.sqrt(x * x + y * y)


def vector(a, b):
    x, y = a
    X, Y = b
    return (X - x, Y - y)


def unit(a):
    x, y = a
    l = length(a)
    return (x / l, y / l)


def distance(A, B):
    return length(vector(A, B))


def scale(a, scalar):
    x, y = a
    return (x * scalar, y * scalar)


def add(a, b):
    x, y = a
    X, Y = b
    return (x + X, y + Y)

def point2line(point, A, B):
    line_vec = vector(A, B)
    pnt_vec = vector(A, point)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/line_len)
    t = dot(line_unitvec, pnt_vec_scaled)
    r=1
    if t < 0.0:
        t = 0.0
        r = -1
    elif t > 1.0:
        t = 1.0
        r = -1
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, A)
    return (dist, (int(nearest[0]), int(nearest[1])),r)