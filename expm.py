from numpy import zeros, ones, array, empty
from expokit import dgpadm

def makef(nstates, ideg=4):
    """
    make a function for exponentiating a nstates-by-nstates transition
    matrix
    """
    ncells = nstates*nstates
    lwsp = 4*ncells + ideg + 1
    ipiv = zeros(nstates, dtype=int)
    wsp = empty(lwsp)
    def f(Q, t, ipiv=ipiv, wsp=wsp):
        x = dgpadm(ideg, t, Q, wsp, ipiv)
        print x
        i = x[0]-1
        print nstates, i
        p = wsp[i:i+ncells].reshape((nstates,nstates))
        return p.T
    return f

for i in range(2, 20):
    q = ones((i,i), dtype=float)
    f = makef(i)
    f(q, 1)

## q = array([[-1,  1,  0,  0,  0],
##            [ 0, -1,  1,  0,  0],
##            [ 0,  0, -1,  1,  0],
##            [ 0,  0,  0, -1,  1],
##            [ 0,  0,  1,  0, -1]], dtype=float)
## f = makef(5)
## f(q, 1)
