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

"""
Generic interface for handling compatibility issues between python 2 and
python3
"""

import abc

import Error
import Platform


platform = Platform.Platform()

if platform.is_python2():
    import __builtin__ as builtins
    ABC = abc.ABCMeta('ABC', (), {})

if platform.is_python3():
    import builtins
    ABC = abc.ABC

def range(*args):
    """
    Wrapper for range usage, returning an iterator regardless of if
    python 2 or python 3 is used
    """
    if len(args) < 1 or len(args) > 3:
        err_msg = "ERROR: Anguilla range function takes 1, 2, or 3 arguments"
        raise Error.Error(msg=err_msg)

    start = 0
    stop = 1
    step = 1

    if len(args) == 1:
        stop = args[0]

    if len(args) == 2:
        start = args[0]
        stop = args[1]
    
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

    if platform.is_python2():
        return builtins.xrange(start, stop, step)
    elif platform.is_python3():
        return builtins.range(start, stop, step)
    else:
        err_msg = "ERROR: Unknown python platform"
        raise Error.Error(msg=err_msg)

def dict_keys(a_dict):
    """
    Returns a list of the keys in a dict
    """
    if platform.is_python2():
        return a_dict.keys()
    elif platform.is_python3():
        return list(a_dict.keys())
    else:
        err_msg = "ERROR: Unknown python platform"
        raise Error.Error(msg=err_msg)

def config_parser():
    """
    Returns a configuration parser
    """
    if platform.is_python2():
        import ConfigParser as conf_parser
    if platform.is_python3():
        import configparser as conf_parser
        
    parser = conf_parser.SafeConfigParser()

    # The following line is needed as all option names are passed through
    # the 'optionxform()' method, whose default implementation converts 
    # option names to lower case.
    # See e.g.
    # http://stackoverflow.com/questions/19359556/configparser-reads-capital-keys-and-make-them-lower-case
    parser.optionxform = str
    
    return parser
