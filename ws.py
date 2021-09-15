#!/usr/bin/env python3
##############################################################
# DESCRIPTION:  Simple WS wrapper so I can test this out in
#                   - Docker
#                   - K8S
##############################################################

import cherrypy
from character_roller import CharacterRoller

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                                               })

class WS(object):
    def GET(self, *args, **kwargs):
        for key in kwargs.keys():
            self.settings[key] = kwargs[key]

    @cherrypy.expose
    def index(self, **kwargs):
        settings = dict([ i for i in cherrypy.request.params.items() ])
        cr = CharacterRoller(settings=settings)
        return cr.main()

cherrypy.quickstart(WS())
