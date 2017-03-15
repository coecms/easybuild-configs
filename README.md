EasyBuild configs for ARCCSS at NCI
===================================

Using
-----

    module use /g/data3/hh5/modules/all/Core
    module load EasyBuild

    eb --configfiles=easybuild.configs --robot .  $LIB.eb

Toolchains
----------

The following toolchains are available:

 * iimkl: icc, ifort, mkl

 * intel: icc, ifort, mkl, intel mpi

 * iomkl: icc, ifort, mkl, open mpi

