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
__author__ = 'Sebastian'

from pylons import request, response, session, tmpl_context as c
from pycloud.pycloud.pylons.lib import helpers as h

from pycloud.pycloud.model.user import User

import hashlib

#####################################################################################################################
# Checks if we have been authenticated. If not, redirects to login page.
#####################################################################################################################
def ensure_authenticated():
    # TODO: remove this, admin user should not be created in this integrated manner. Or should it?
    create_admin_user()

    user = session.get('user')
    if not user:
        return h.redirect_to(controller='auth', action='signin_form')

#####################################################################################################################
# Authenticates a user. If it doesn't work, returns to login page.
#####################################################################################################################
def authenticate():
    if len(request.params) > 1:
        user = User.by_username(request.params['username'])
        if user:
            # Compare a hash of the given password with the stored hash.
            hashed_password = hashlib.sha256(request.params['password']).hexdigest()
            stored_password = user.hashed_pwd

            if stored_password == hashed_password:
                session['user'] = request.params['username']
                session.save()
                return h.redirect_to(controller='home', action='index')

    # Else for all ifs..
    h.flash('Invalid credentials.')
    return h.redirect_to(controller='auth', action='signin_form')

#####################################################################################################################
# Clears out the logged in user.
#####################################################################################################################
def signout():
    session.clear()
    session.save()

#####################################################################################################################
# Creates a default admin user.
#####################################################################################################################
def create_admin_user():
    admin_username = 'admin'
    user = User.by_username(admin_username)
    if not user:
        print 'Creating admin user'
        admin_user = User()
        admin_user.username = admin_username
        admin_user.hashed_pwd = hashlib.sha256('admin.123').hexdigest()
        admin_user.save()
