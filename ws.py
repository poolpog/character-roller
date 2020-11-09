#!/usr/bin/env python3
##############################################################
# DESCRIPTION:  Simple WS wrapper so I can test this out in
#                   - Docker
#                   - K8S
##############################################################

import cherrypy
import character_roller

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                                               })

class WS(object):
    @cherrypy.expose
    def index(self):
        return character_roller.main(output_format="json")

cherrypy.quickstart(WS())
