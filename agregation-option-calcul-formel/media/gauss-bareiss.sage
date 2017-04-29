m = matrix([[2,1,3],[1,4,9],[1,8,27]])
def gauss_bareiss(m):
    m = copy(m)
    n = m.nrows()
    a = 1
    for i in range(n):
        print m
        print
        assert m[i,i]!=0
        for j in range(i+1, n):
            m[j] = (m[i,i] * m[j] - m[j,i]*m[i]) / a
        a = m[i,i]
    return m
