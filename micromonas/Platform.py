#
# micromonas
#
#
# BSD 3-Clause License
#
# Copyright (c) 2018, Magnus Gyllin
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import platform

import RandomSeed


class Platform():
    """
    Class for providing info on the underlying platform
    """
    def __init__(self):
        """
        Class constructor
        """
        self._system_name = platform.system()
        self._system_info = platform.platform()
        self._python_version = platform.python_version()
        self._python_implementation = platform.python_implementation()
        
        major_ver = self._python_version.split(".")[0]
        self._ispython2 = (major_ver == "2")
        self._ispython3 = (major_ver == "3")
        
        self._random_seed = RandomSeed.RandomSeed()
    
    def is_linux(self):
        """
        Returns True if on a linux platform, False otherwise
        """
        if self._system_name == "Linux":
            return True
        else:
            return False
    
    def is_python2(self):
        """
        Returns True if python major version is 2, False otherwise
        """
        return self._ispython2

    def is_python3(self):
        """
        Returns True if python major version is 3, False otherwise
        """
        return self._ispython3

    def system(self):
        """
        Returns a string with system information
        """
        return self._system_info
    
    def python_version(self):
        """
        Returns the Python version as string "major.minor.patchlevel"
        """
        return self._python_version
    
    def python_implementation(self):
        """
        Returns a string identifying the Python implementation
        """
        return self._python_implementation
    
    def get_random_seed(self):
        """
        Returns the random seed
        """
        return self._random_seed
    
    def refresh_random_seed(self):
        """
        Refreshes the random seed
        """
        self._random_seed.refresh()
