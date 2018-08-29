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

import LogFile
import OS
import Error
import TimeStamp


class TestLogFile():
    """ 
    Class for testing the handling of log files in micromonas
    """
    def __init__(self):
        self._os = OS.OS()
        self._ts = TimeStamp.TimeStamp()
        self._existing_log_file = "mocks/test.log"

    @classmethod
    def setup_class(self):
        pass
 
    @classmethod
    def teardown_class(self):
        pass

    def constructor_1st_test(self):
        log_file_name = "LogFile_constructor_1st_test.log"

        LogFile.LogFile(log_file_name, self._ts)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip whitespaces
        content = [x.strip() for x in content]

        first_line = content[0]

        first_word = first_line.split(" ")[0]

        nose.tools.assert_equal("Generated", first_word)

        self._os.remove(log_file_name)

    @nose.tools.raises(Error.Error)
    def constructor_2nd_test(self):
        LogFile.LogFile(self._existing_log_file, self._ts)
    
    def append_1st_test(self):
        log_file_name = "LogFile_append_1st_test.log"
        line = "Appended line"

        log = LogFile.LogFile(log_file_name, self._ts)
        log.append(line)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip whitespaces
        content = [x.strip() for x in content]

        nose.tools.assert_equal(line, content[-1])

        self._os.remove(log_file_name)

    def append_tabbed_1st_test(self):
        log_file_name = "LogFile_append_tabbed_1st_test.log"
        line = "Appended line"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        log.append_tabbed(line)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip trailing whitespaces
        content = [x.rstrip() for x in content]

        nose.tools.assert_equal("\t"+line, content[-1])

        self._os.remove(log_file_name)

    def append_tabbed_2nd_test(self):
        log_file_name = "LogFile_append_tabbed_2nd_test.log"
        line = "Appended line"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        log.append_tabbed(line, no_of_tabs=3)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip trailing whitespaces
        content = [x.rstrip() for x in content]

        nose.tools.assert_equal("\t\t\t"+line, content[-1])

        self._os.remove(log_file_name)
    
    @nose.tools.raises(Error.Error)
    def append_tabbed_3rd_test(self):
        log_file_name = "LogFile_append_tabbed_3rd_test.log"
        line = "Appended line"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        
        try:
            log.append_tabbed(line, no_of_tabs=0)
        except Error.Error as e:
            try:
                self._os.remove(log_file_name)
            except Error as e:
                print("TEST ERROR: Unable to delete log file '%s'" % e.filename)
            raise e

    def append_section_name_1st_test(self):
        log_file_name = "LogFile_append_section_name_1st_test.log"
        sec_name = "Test section"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        
        log.append_section_name(sec_name)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip whitespaces
        content = [x.strip() for x in content]
        
        control_string = "============"
        nose.tools.assert_equal(control_string, content[-2])

        self._os.remove(log_file_name)
        
    def append_subsection_name_1st_test(self):
        log_file_name = "LogFile_append_subsection_name_1st_test.log"
        sub_sec_name = "Test subsection"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        
        log.append_subsection_name(sub_sec_name)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip whitespaces
        content = [x.strip() for x in content]
        
        control_string = "---------------"
        nose.tools.assert_equal(control_string, content[-1])

        self._os.remove(log_file_name)
        
    def cat_1st_test(self):
        log_file_name = "LogFile_cat_1st_test.log"
        
        log = LogFile.LogFile(log_file_name, self._ts)
        
        log.cat(self._existing_log_file)
        
        with open(log_file_name) as f:
            content = f.readlines()
        
        # Strip whitespaces
        content = [x.strip() for x in content]

        nose.tools.assert_equal("Generated YYYY-MM-DD HH:MM:SS", content[-2])
        
        self._os.remove(log_file_name)
