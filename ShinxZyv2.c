def pungsi(int N):

    cdef int i,j

    j=0

    for i in range(N):

        j=i+100

        if(j%2==0):

            j+=i

        while(j>N/10):

            j-=10

        continue

    return i+j
from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize(“fCython.pyx”))
import time

from numba import jit

from fCython import pungsi as pungsiCython


def pungsi(N):

    j=0

    for i in range(N):

        j=i+100

        if(j%2==0):

            j+=i

        while(j>N/10):

            j-=10

        continue

    return i+j


N=1000000;

start=time.time()

hasil=pungsi(N)

print(‘Pythonic Waktu: %.8f seconds, hasil=%d’ %((time.time()–start),hasil))

pungsi_jit=jit(pungsi)

start=time.time()

hasil=pungsi_jit(N)

print(‘JIT Waktu: %.8f seconds, hasil=%d’ %((time.time()–start),hasil))

start=time.time()

hasil=pungsiCython(N)

print(‘Cython Waktu: %.8f seconds, hasil=%d’ %((time.time()–start),hasil))
