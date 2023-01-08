import sys
import os

# Available at setup time due to pyproject.toml
# from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)



ext_modules = [
    Pybind11Extension("ventura_dlopen",
                      ["ventura_dlopen/main.cpp"],
                      define_macros=[('VERSION_INFO', __version__)],
                      library_dirs=os.environ['LSST_LIBRARY_PATH'].split(":"),
                      libraries=[
                          # conda libs
                          "cfitsio",
                          "gsl",
                          "blas",
                          "Minuit2",
                          "log4cxx",
                          "boost_math_c99",
                          "ast",
                          "ast_pal",
                          "ast_cminpack",
                          "ast_grf_2.0.9",
                          "ast_grf_3.2.9",
                          "ast_grf_5.6.9",
                          "ast_grf3d",
                          "ast_err",
                          "yaml",
                          "fftw3f",
                          "fftw3",
                          # lsst libs
                          "meas_algorithms",
                          "meas_base",
                          "afw",
                          "log",
                          "daf_base",
                          "geom",
                          "sphgeom",
                          "cpputils",
                          "pex_exceptions",
                          "base",
                          "astshim",
                      ]
                      ),
]

# Need to modify LDFLAGS to remove -Wl,-dead_strip_dylibs
# Need library_dirs for our stuff.

setup(
    name="ventura_dlopen",
    version=__version__,
    author="Eli Rykoff",
    author_email="erykoff@gmail.com",
    url="https://github.com/erykoff/ventura_dlopen",
    description="A test project using pybind11 to crash on ventura",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
