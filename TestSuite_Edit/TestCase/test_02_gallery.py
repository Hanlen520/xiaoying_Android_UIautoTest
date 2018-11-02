#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import creation,camera,login,gallery
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name()

class Gallery_Action(unittest.TestCase, BasePage):
    '''gallery的测试'''
    @setup
    def setUp(self):
        self.d.app_start(pkg_name)

    @teardown
    def tearDown(self):
        self.d.app_stop(pkg_name)


