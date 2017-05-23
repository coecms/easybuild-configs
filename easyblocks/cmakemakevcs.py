#!/usr/bin/env python
"""
Copyright 2017 ARC Centre of Excellence for Climate Systems Science

author: Scott Wales <scott.wales@unimelb.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from easybuild.easyblocks.generic.cmakemake import CMakeMake
from easybuild.tools.run import run_cmd
from easybuild.tools.config import source_paths
from easybuild.tools.filetools import rmtree2, mkdir
from easybuild.framework.easyconfig.easyconfig import letter_dir_for
import tempfile
import os.path

class CMakeMakeVcs(CMakeMake):
    """
    Download source using svn
    """

    def obtain_file(self, filename, extension=False, urls=None):
        """
        Fetch the source files from svn
        """

        if filename.startswith('svn+'):
            # Export the repository and convert to a tarball
            download_path = os.path.join(source_paths()[0], letter_dir_for(self.name), self.name)
            tarfile = os.path.basename(filename)+'.tar.gz'
            fullpath = os.path.join(download_path, tarfile)

            if os.path.exists(fullpath):
                return fullpath

            mkdir(download_path, parents=True)
            tempdir = tempfile.mkdtemp()
            run_cmd("svn export %s"%filename[4:], path = tempdir)
            run_cmd("tar czvf %s ."%fullpath, path = tempdir)
            rmtree2(tempdir)
            return fullpath

        elif filename.startswith('git+'):
            # Export the repository and convert to a tarball
            (url, treeish) = filename[4:].split()

            download_path = os.path.join(source_paths()[0], letter_dir_for(self.name), self.name)
            tarfile = treeish+'.tar'
            fullpath = os.path.join(download_path, tarfile)

            mkdir(download_path, parents=True)
            run_cmd("git archive --format=tar --prefix=src/ --output='%s' --remote='%s' '%s'"%(fullpath, url, treeish))
            return fullpath

        else:
            # Defer to default downloader
            return super(self, CMakeMakeSvn).obtain_file(self, filename, extension, urls)



