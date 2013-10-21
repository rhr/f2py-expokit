from numpy import zeros, ones, array, empty
from scipy.linalg import expm
from expokit import dmexpv, dgpadm

def dexpm(h, t):
    ideg = 4
    nstates = h.shape[0]
    lwsp = 4*nstates**2+ideg+1
    ipiv = zeros(nstates, dtype=int)
    hsize = nstates**2
    wsp = empty(lwsp)
    i = dgpadm(ideg, t, h, wsp, ipiv)[0]-1
    print 'i =', i
    p = wsp[i:i+hsize].reshape(h.shape)
    return p.T


q = array([[-1,  1, 0],
           [ 0, -1, 1],
           [ 0,  0, 0]], dtype=float)

print dexpm(q,1)
print
print expm(q)
