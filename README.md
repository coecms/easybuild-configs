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

 * iccifort: icc, ifort

 * iimkl: icc, ifort, mkl

 * intel: icc, ifort, mkl, intel mpi

 * iomkl: icc, ifort, mkl, open mpi

To build with a different toolchain:

    eb ... --try-toolchain-name=intel

Implementation Details
----------------------

The compiler and MPI modules have two implementations. This is because
Easybuild expects specific names for the modules, but we also want to be
consistent with the existing NCI setup.

The Easybuild modules 'icc', 'ifort', 'impi' and 'OpenMPI' are no-ops, with the
sole function of setting up the module naming heirachy. They are hidden in the
module list and shouldn't be used directly by users.

The NCI names 'intel-cc', 'intel-fc', 'intel-mpi' and 'openmpi' load the
Easybuild modules to set the correct paths and then load the original NCI
modules.

This means that if a user runs `module load intel-fc` their `MODULEPATH` will
be updated to include `Compiler/Intel/$INTELFC_VERSION` and they will have
access to `ifort`.
