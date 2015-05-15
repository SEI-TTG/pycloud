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

from pylons import config
from pycloud.pycloud.pylons.lib.app_globals import Globals
from pycloud.pycloud.cloudlet import get_cloudlet_instance
from pycloud.pycloud.pylons.lib import helpers
from mako.lookup import TemplateLookup
import os


def load_environment(make_map_function, root_path, global_conf={}, app_conf={}):

    paths = {'root': root_path,
             'controllers': os.path.join(root_path, 'controllers'),
             'templates': [os.path.join(root_path, 'templates')],
             'static_files': os.path.join(root_path, 'public')
    }
    
    print 'Templates path: ' + os.path.join(root_path, 'templates')

    config.init_app(global_conf, app_conf, package='pycloud', paths=paths)

    config['routes.map'] = make_map_function()
    config['debug'] = True
    config['pylons.g'] = Globals()
    config['pylons.h'] = helpers

    # Clean up the system. This must be called after the object is already created
    get_cloudlet_instance().cleanup_system()

    config["pylons.g"].mako_lookup = TemplateLookup(
        directories=paths["templates"],
        input_encoding="utf-8",
        imports=[
            "from pylons import c, g, request",
            "from pylons.i18n import _, ungettext",
            "from pycloud.pycloud.pylons.lib import helpers as h",
            "from routes import url_for"
            ]
    )