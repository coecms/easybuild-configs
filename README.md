EasyBuild configs for ARCCSS at NCI
===================================

Using
-----

    module use /g/data3/hh5/modules/all/Core
    module load EasyBuild

    eb --configfiles=easybuild.configs $LIB.eb

Toolchains
----------

The following toolchains are available in the `toolchains` directory

 * iimkl: icc, ifort, mkl

 * intel: icc, ifort, mkl, intel mpi

 * iomkl: icc, ifort, mkl, open mpi

These make use of packages in the `system` directory, each of which is a
wrapper around a NCI module
