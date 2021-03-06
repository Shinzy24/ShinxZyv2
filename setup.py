from setuptools import setup, Extension, find_packages

RELEASE_VERSION = '0.0.8'

c_lib = Extension(
    'circularbuffer',
    sources=[
        'src/ShinxZyv2.c',
        
    ],
    include_dirs=['src'],
)

setup(
    name='pycircularbuffer',
    version=RELEASE_VERSION,
    url='https://github.com/dozymoe/PyCircularBuffer',
    download_url='https://github.com/dozymoe/PyCircularBuffer/tarball/' +\
            RELEASE_VERSION,

    author='muhammad Zainul umam',
    author_email='Ekaarsana249@gmail.com',
    description='Simple implementation of circular buffer.',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=[],
    ext_modules=[c_lib],
)
