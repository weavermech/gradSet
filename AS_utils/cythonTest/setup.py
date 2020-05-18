from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("/home/weaver/PycharmProjects/pytorch-grad-semseg/py2cy/gtThresh.pyx"))