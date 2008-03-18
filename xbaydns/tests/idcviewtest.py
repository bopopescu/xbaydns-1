#!/usr/bin/env python
# encoding: utf-8
"""
idcviewtest.py

Created by QingFeng on 2008-03-17.
Copyright (c) 2007 xBayDNS Team. All rights reserved.
"""

import basetest
import logging.config
import os
import pwd
import shutil
import tempfile
import time
import unittest

log = logging.getLogger('xbaydns.tests.idcviewtest')
#logging.basicConfig(level=logging.DEBUG)

from xbaydns.tools import idcview

class LogToListTest(basetest.BaseTestCase):
    def setUp(self):
        """初始化测试环境"""
        self.basedir = os.path.realpath(tempfile.mkdtemp(suffix='xbaydns_test'))
        basetest.BaseTestCase.setUp(self)
        self.__initfile()

    def tearDown(self):
        """清洁测试环境"""
        shutil.rmtree(self.basedir)
        basetest.BaseTestCase.tearDown(self)
        self.__rmfile()
        
    def __initfile(self):
        f=open('/tmp/10.10.10.10_20080317','w')
        f.write('10.10.10.20,ping,0.905,2008-03-17 00:00:00\n')
        f.write('10.10.10.21,pinggate,0.791,2008-03-17 00:00:00\n')
        f.write('10.10.10.22,pinggate,0.985,2008-03-17 00:00:00\n')
        f.write('10.10.10.20,nslookup,0.836,2008-03-17 00:05:00\n')
        f.write('10.10.10.21,pinggate,0.715,2008-03-17 00:05:00\n')
        f.write('10.10.10.22,ping,0.805,2008-03-17 00:05:00\n')
        f.close()
        f=open('/tmp/11.11.11.11_20080317','w')
        f.write('20.10.10.20,ping,0.605,2008-03-17 00:00:00\n')
        f.write('20.10.10.21,pinggate,0.991,2008-03-17 00:00:00\n')
        f.write('20.10.10.22,pinggate,0.995,2008-03-17 00:00:00\n')
        f.write('20.10.10.20,nslookup,0.896,2008-03-17 00:05:00\n')
        f.write('20.10.10.21,pinggate,0.605,2008-03-17 00:05:00\n')
        f.write('20.10.10.22,ping,0.405,2008-03-17 00:05:00\n')
        f.close()
    def __rmfile(self):
        os.remove('/tmp/10.10.10.10_20080317')
        os.remove('/tmp/11.11.11.11_20080317')
        
    def test_convfiles(self):
        files=['/tmp/10.10.10.10_20080317','/tmp/11.11.11.11_20080317']
        data=idcview.convfiles(files)
        self.assertTrue(isinstance(data,list))
        print data

def suite():
    """集合测试用例"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LogToListTest, 'test'))
    return suite

"""
单独运行command的测试用例
"""
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
