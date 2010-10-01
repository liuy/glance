# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Parallax API controllers.
"""

import json
import time

import routes
import webob.dec
import webob.exc
import webob

from glance.common import flags
from glance.common import utils
from glance.common import wsgi
from glance.parallax.api import images


FLAGS = flags.FLAGS


class API(wsgi.Router):
    """WSGI entry point for all Parallax requests."""

    def __init__(self):
        # TODO(sirp): should we add back the middleware for parallax
        mapper = routes.Mapper()
        mapper.resource("image", "images", controller=images.Controller(),
                        collection={'detail': 'GET'})
        super(API, self).__init__(mapper)
