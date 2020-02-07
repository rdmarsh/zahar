#!/usr/bin/env python3

#    zart Zabbix API Retrieval Tool.
#    Copyright (C) 2020 David Marsh
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

__project__ = 'zahar'
__appname__ = 'zart'
__appdesc__ = 'Zabbix API Retrieval Tool'
__version__ = '0.3'
__author__ = 'David Marsh'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2020 David Marsh'
__url__ = 'https://github.com/rdmarsh/zahar'


from pyzabbix import ZabbixAPI
import os
import sys
import click
import click_config_file
import socket
import socks


from apiclasses import action
from apiclasses import alert
from apiclasses import apiinfo
from apiclasses import application
from apiclasses import autoregistration
from apiclasses import correlation
from apiclasses import dashboard
from apiclasses import dcheck
from apiclasses import dhost
from apiclasses import drule
from apiclasses import dservice
from apiclasses import event
from apiclasses import graph
from apiclasses import graphitem
from apiclasses import graphprototype
from apiclasses import history
from apiclasses import host
from apiclasses import hostgroup
from apiclasses import hostinterface
from apiclasses import hostprototype
from apiclasses import httptest
from apiclasses import iconmap
from apiclasses import image
from apiclasses import item
from apiclasses import itemprototype
from apiclasses import maintenance
from apiclasses import map
from apiclasses import mediatype
from apiclasses import problem
from apiclasses import proxy
from apiclasses import screen
from apiclasses import screenitem
from apiclasses import script
from apiclasses import service
from apiclasses import servicesla
from apiclasses import template
from apiclasses import templatescreen
from apiclasses import templatescreenitem
from apiclasses import trend
from apiclasses import trigger
from apiclasses import triggerprototype
from apiclasses import user
from apiclasses import usergroup
from apiclasses import usermacro
from apiclasses import usermedia
from apiclasses import valuemap

config_file=os.path.join(click.get_app_dir(__project__,force_posix=True), 'config.ini')

class Zart(object):
    def __init__(self, zapi, apiv):
        self.zapi = zapi
        self.apiv = apiv


@click.group(epilog='default config file: ' + click.format_filename(config_file))
@click_config_file.configuration_option(config_file_name=config_file)
@click.option('--zaburl', help='Zabbix URL.')
@click.option('--userid', help='Zabbix username.')
@click.option('--passwd', help='Zabbix password.')
@click.option('--proxy', type=(str, int),
              default=(None, 1080), metavar='<HOST PORT>',
              help='Socks5 proxy address and port.')
# todo: add a flag to show the api version and exit
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, zaburl, userid, passwd, proxy):
    """
    zart Zabbix API Retrieval Tool.
    """

    if not zaburl or not userid or not passwd:
        click.secho('Error: zaburl, userid or passwd not set via cli or in config file', fg='red', err=True)
        click.secho('Default config file: ' + click.format_filename(config_file), fg='red', err=True)
        sys.exit(1)

    if proxy and None not in proxy:
        socks.set_default_proxy(socks.SOCKS5, proxy[0], proxy[1])
        socket.socket = socks.socksocket

    zapi = ZabbixAPI(zaburl)
    zapi.login(userid, passwd)
    apiv = zapi.apiinfo.version()
    ctx.obj = Zart(zapi, apiv)


cli.add_command(action.action)
cli.add_command(alert.alert)
cli.add_command(apiinfo.apiinfo)
cli.add_command(application.application)
cli.add_command(autoregistration.autoregistration)
cli.add_command(correlation.correlation)
cli.add_command(dashboard.dashboard)
cli.add_command(dcheck.dcheck)
cli.add_command(dhost.dhost)
cli.add_command(drule.drule)
cli.add_command(dservice.dservice)
cli.add_command(event.event)
cli.add_command(graph.graph)
cli.add_command(graphitem.graphitem)
cli.add_command(graphprototype.graphprototype)
cli.add_command(history.history)
cli.add_command(host.host)
cli.add_command(hostgroup.hostgroup)
cli.add_command(hostinterface.hostinterface)
cli.add_command(hostprototype.hostprototype)
cli.add_command(httptest.httptest)
cli.add_command(iconmap.iconmap)
cli.add_command(image.image)
cli.add_command(item.item)
cli.add_command(itemprototype.itemprototype)
cli.add_command(maintenance.maintenance)
cli.add_command(map.map)
cli.add_command(mediatype.mediatype)
cli.add_command(problem.problem)
cli.add_command(proxy.proxy)
cli.add_command(screen.screen)
cli.add_command(screenitem.screenitem)
cli.add_command(script.script)
cli.add_command(service.service)
cli.add_command(servicesla.servicesla)
cli.add_command(template.template)
cli.add_command(templatescreen.templatescreen)
cli.add_command(templatescreenitem.templatescreenitem)
cli.add_command(trend.trend)
cli.add_command(trigger.trigger)
cli.add_command(triggerprototype.triggerprototype)
cli.add_command(user.user)
cli.add_command(usergroup.usergroup)
cli.add_command(usermacro.usermacro)
cli.add_command(usermedia.usermedia)
cli.add_command(valuemap.valuemap)

if __name__ == '__main__':
    cli()
