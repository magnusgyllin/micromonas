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

import nose.tools

import OS
import Error


class TestOS():
    """ 
    A class for testing the handling of miscellaneous operating system 
    operations in micromonas
    """
    def __init__(self):
        self._os = OS.OS()
        self._existing_file = "mocks/test.log"
        self._non_existing_file = "mocks/non_existing_file"

    @classmethod
    def setup_class(self):
        pass
 
    @classmethod
    def teardown_class(self):
        pass

    def is_file_1st_test(self):
        result = self._os.is_file(self._existing_file)
        nose.tools.assert_true(result)

    def is_file_2nd_test(self):
        result = self._os.is_file(self._non_existing_file)
        nose.tools.assert_false(result)
    
    def remove_1st_test(self):
        file_name = "OS_remove_1st_test.test"
        
        with open(file_name, "w") as f:
            f.write("\n")
        
        self._os.remove(file_name)
        
        result = self._os.is_file(file_name)
        nose.tools.assert_false(result)
    
    @nose.tools.raises(Error.Error)
    def remove_2nd_test(self):
        self._os.remove(self._non_existing_file)
