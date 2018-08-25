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

import random
import time

import Error
import Compatibility


class RNG():
    """
    Class for handling of random number generators
    """
    def __init__(self, seed=None):
        self._n_warm_up_cycles = 10**6
        
        if seed != None:
            try:
                self._rng = random.Random(seed)
            except (ValueError, TypeError):
                err_msg = ("ERROR: Cannot construct random number generator " +
                           "with seed '%s'" % seed)
                raise Error.Error(msg=err_msg)
            self._rng = random.Random(seed)
        else:
            seed = time.time()
            self._rng = random.Random(seed)
            for i in Compatibility.range(self._n_warm_up_cycles):
                self._rng.random()
            
    def get_state(self):
        """
        Returns the state of the random number generator
        """
        return self._rng.getstate()
    
    def rand_int(self, a, b):
        """
        Returns a random integer N such that a <= N <= b
        """
        return self._rng.randint(a, b)
    
    def rand_float(self):
        """
        Returns a floating point number in the range [0.0, 1.0)
        """
        return self._rng.random()
    
    def shuffle(self, x):
        """
        Returns a list of the shuffled elements of the sequence x
        """
        return self._rng.sample(x, k=len(x))
    
    def sample_without_repl(self, x, k):
        """
        Returns a list with k elements of the sequence x, sampled without
        replacement
        """
        return self._rng.sample(x, k)
    
    def sample_with_repl(self, x, k):
        """
        Returns a list with k elements of the sequence x, sampled with
        replacement
        """
        hi_idx = len(x) - 1
        return [x[self.rand_int(0, hi_idx)] for _ in Compatibility.range(k)]
