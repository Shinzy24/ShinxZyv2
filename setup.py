import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext = Extension("Random-ip", sources=["Random-ip.c"])

setup(
	ext_modules=[ext],
	cmdclass={"build_ext": build_ext}
)

try:
	os.system("rm -rf build")
except:
	pass