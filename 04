
def strassen(A, B):
    a, b = A[0]
    c, d = A[1]
    e, f = B[0]
    g, h = B[1]

    m1 = (a+d)*(e+h)
    m2 = (c+d)*e
    m3 = a*(f-h)
    m4 = d*(g-e)
    m5 = (a+b)*h
    m6 = (c-a)*(e+f)
    m7 = (b-d)*(g+h)

    return [[m1+m4-m5+m7, m3+m5],
            [m2+m4, m1+m3-m2+m6]]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Product Matrix:")
print(*strassen(A, B), sep="\n")
