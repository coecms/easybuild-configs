#!/usr/bin/env python

from easybuild.framework.easyblock import EasyBlock
from easybuild.framework.easyconfig import MANDATORY, CUSTOM
from easybuild.tools.environment import setvar
from easybuild.tools.run import run_cmd

class Fcm(EasyBlock):

    @staticmethod
    def extra_options(extra_vars = None):
        extra_vars = EasyBlock.extra_options(extra_vars)
        extra_vars.update({
            'fcm_config': [None, "FCM Configuration file to build from", MANDATORY],
            'build_environment': [None, "Environment variables while building", CUSTOM],
            })
        return extra_vars

    def configure_step(self):
        pass

    def build_step(self):
        for k, v in self.cfg['build_environment'].items():
            setvar(k, v)
        run_cmd('fcm make -f %s'%self.cfg['fcm_config'])

    def install_step(self):
        run_cmd('install -d %s/lib'%(self.installdir))
        run_cmd('install -d %s/include'%(self.installdir))

        run_cmd('install -t %s/lib %s/build/lib/*.a'%(self.installdir, self.builddir))
        run_cmd('install -t %s/include %s/build/include/*.mod'%(self.installdir, self.builddir))
