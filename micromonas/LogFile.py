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

import shutil

import Platform
import OS
import TimeStamp
import Error


class LogFile():
    """ 
    Class for handling of log files

    Caution is advised when using this class in a parallel execution 
    mode, as it is not really designed for that
    """
    def __init__(self, name, time_stamp, header=None):
        self._platform = Platform.Platform()
        self._os = OS.OS()
        self._name = name
        self._ERR_FILE_EXIST = "ERROR: Log file '%s' already exists" % name
        self._ERR_FILE_OPEN = "ERROR: Unable to open log file '%s'" % name
        
        if self._os.is_file(name):
            raise Error.Error(msg=self._ERR_FILE_EXIST)
        else:
            try:
                f = open(name, 'w')
            except IOError:
                raise Error.Error(msg=self._ERR_FILE_OPEN)
            
            if header != None:
                f.write("%s\n" % header)

            line = "Generated %s" % time_stamp.as_string()
            f.write(line+"\n\n")
            line = "System: %s" % self._platform.system()
            f.write(line+"\n")
            line = "Python version: %s" % self._platform.python_version()
            f.write(line+"\n")
            line = ("Python implementation: %s" 
                    % self._platform.python_implementation())
            f.write(line+"\n\n")
            f.close()

    def append(self, msg):
        """
        Appends <msg> to the log file. A trailing newline is added.
        """
        try:
            f = open(self._name, 'a')
        except IOError:
            raise Error.Error(msg=self._ERR_FILE_OPEN)
        f.write(msg+"\n")
        f.close()
    
    def append_tabbed(self, msg, no_of_tabs=1):
        if no_of_tabs > 0:
            tabs = ""
            for i in range(no_of_tabs):
                tabs = tabs+"\t"
            
            self.append(tabs+msg)
        else:
            err_msg = "ERROR: Tabbed append to log file need one or more tabs"
            raise Error.Error(err_msg)
    
    def append_section_name(self, section_name):
        """
        Appends a section name, i.e. the <section name> with double
        underlining, to the log file
        """
        underlinings = "="*len(section_name)
        msg = "\n\n%s\n%s\n" % (section_name, underlinings)
        self.append(msg)
    
    def append_subsection_name(self, subsection_name):
        """
        Appends a subsection name, i.e. the <subsection name> with single
        underlining, to the log file
        """
        underlinings = "-"*len(subsection_name)
        msg = "\n%s\n%s" % (subsection_name, underlinings)
        self.append(msg)
    
    def cat(self, file_name):
        """
        Appends the content of <file_name> to the log file
        """
        try:
            f = open(self._name, 'a')
        except IOError:
            raise Error.Error(msg=self._ERR_FILE_OPEN)

        try:
            fd = open(file_name, 'r')
        except IOError:
            f.close()
            err_msg = ("ERROR: Unable to open file '%s' for cat operation" % 
                       file_name)
            raise Error.Error(msg=err_msg)

        shutil.copyfileobj(fd, f)
        f.close()
        fd.close()
