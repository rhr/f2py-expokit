# replace 'call matvec(' with 'call matvec(n, ' in expokit.orig.f
f2py -m expokit -h expokit.pyf expokit.f
f2py -c expokit.pyf expokit.f --link-lapack --link-blas
