# KVM-based Discoverable Cloudlet (KD-Cloudlet) 
# Copyright (c) 2015 Carnegie Mellon University.
# All Rights Reserved.
# 
# THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER. CARNEGIE MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT PERMITTEDBY LAW ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY RIGHTS.
# 
# Released under a modified BSD license, please see license.txt for full terms.
# DM-0002138
# 
# KD-Cloudlet includes and/or makes use of the following Third-Party Software subject to their own licenses:
# MiniMongo
# Copyright (c) 2010-2014, Steve Lacy 
# All rights reserved. Released under BSD license.
# https://github.com/MiniMongo/minimongo/blob/master/LICENSE
# 
# Bootstrap
# Copyright (c) 2011-2015 Twitter, Inc.
# Released under the MIT License
# https://github.com/twbs/bootstrap/blob/master/LICENSE
# 
# jQuery JavaScript Library v1.11.0
# http://jquery.com/
# Includes Sizzle.js
# http://sizzlejs.com/
# Copyright 2005, 2014 jQuery Foundation, Inc. and other contributors
# Released under the MIT license
# http://jquery.org/license

__author__ = 'jdroot'

from pymongo.collection import Collection
from cursor import MongoCursor


class MongoCollection(Collection):

    def __init__(self, *args, **kwargs):

        self.obj_class = kwargs.pop('obj_class')

        super(MongoCollection, self).__init__(*args, **kwargs)

    def find(self, *args, **kwargs):
        return MongoCursor(self, *args, obj_class=self.obj_class, **kwargs)

    def find_one(self, *args, **kwargs):
        document = super(MongoCollection, self).find_one(*args, **kwargs)
        if document:
            return self.obj_class(document)
        return None

    def find_and_modify(self, *args, **kwargs):
        document = super(MongoCollection, self).find_and_modify(*args, **kwargs)
        if document:
            return self.obj_class(document)
        return None