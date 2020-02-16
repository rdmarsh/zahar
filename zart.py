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


import os
import sys
import logging
import click
import click_config_file
import socket
import socks
from pyzabbix import ZabbixAPI

from commands import action
from commands import alert
from commands import apiinfo
from commands import application
from commands import autoregistration
from commands import correlation
from commands import dashboard
from commands import dcheck
from commands import dhost
from commands import discoveryrule
from commands import drule
from commands import dservice
from commands import event
from commands import graph
from commands import graphitem
from commands import graphprototype
from commands import history
from commands import host
from commands import hostgroup
from commands import hostinterface
from commands import hostprototype
from commands import httptest
from commands import iconmap
from commands import image
from commands import item
from commands import itemprototype
from commands import maintenance
from commands import map
from commands import mediatype
from commands import problem
from commands import proxy
from commands import screen
from commands import screenitem
from commands import script
from commands import service
from commands import servicesla
from commands import template
from commands import templatescreen
from commands import templatescreenitem
from commands import trend
from commands import trigger
from commands import triggerprototype
from commands import user
from commands import usergroup
from commands import usermacro
from commands import usermedia
from commands import valuemap

root_logger = logging.getLogger()
config_file = os.path.join(click.get_app_dir(__project__, force_posix=True), 'config.ini')


class Zart(object):
    def __init__(self, config_file, zapi, apiv, out_fmt, export_filename):
        self.config_file = config_file
        self.zapi = zapi
        self.apiv = apiv
        self.out_fmt = out_fmt
        self.export_filename = export_filename


@click.group(epilog='default config file: ' + click.format_filename(config_file))
@click_config_file.configuration_option(config_file_name=config_file)
@click.option('-z', '--zab_url', help='Zabbix URL.')
@click.option('-u', '--zab_usr', help='Zabbix username.')
@click.option('-p', '--zab_pwd', help='Zabbix password.')
@click.option('-s', '--sck_prx', type=(str, int), default=(None, 1080), metavar='<HOST PORT>', help='Socks5 proxy address and port.')
@click.option('-o', '--out_fmt', default='txt', type=click.Choice(['csv', 'html', 'pretty-html', 'json', 'pretty-json', 'latex', 'raw', 'txt']), help='Output format.')
@click.option('-v', '--verbose', count=True, help='Be more verbose, -v is INFO, -vv is DEBUG')
@click.option('-x', '--export', 'export_filename', type=click.File('w'), help='Export the query to FILENAME')
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, zab_url, zab_usr, zab_pwd, sck_prx, out_fmt, verbose, export_filename):
    """
    zart Zabbix API Retrieval Tool.
    """

    if verbose >= 2:
        root_logger.setLevel(logging.DEBUG)
    elif verbose == 1:
        root_logger.setLevel(logging.INFO)
    else:
        root_logger.setLevel(logging.WARNING)

    if not zab_url or not zab_usr or not zab_pwd:
        click.secho('Error: zabbix url, username or password not set via cli or in config file', fg='red', err=True)
        click.secho('Default config file: ' + click.format_filename(config_file), fg='red', err=True)
        sys.exit(1)

    if sck_prx and None not in sck_prx:
        socks.set_default_proxy(socks.SOCKS5, sck_prx[0], sck_prx[1])
        socket.socket = socks.socksocket
        logging.info('proxy: %s:%s', sck_prx[0], sck_prx[1])

    zapi = ZabbixAPI(zab_url)
    zapi.login(zab_usr, zab_pwd)
    apiv = zapi.apiinfo.version()
    logging.info('api version: %s', apiv)
    ctx.obj = Zart(config_file, zapi, apiv, out_fmt, export_filename)


cli.add_command(action.action)
cli.add_command(alert.alert)
cli.add_command(apiinfo.apiinfo)
cli.add_command(application.application)
cli.add_command(autoregistration.autoregistration)
cli.add_command(correlation.correlation)
cli.add_command(dashboard.dashboard)
cli.add_command(dcheck.dcheck)
cli.add_command(dhost.dhost)
cli.add_command(discoveryrule.discoveryrule)
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
