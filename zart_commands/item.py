import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve items')
@options.add_options(options.itemids)
@options.add_options(options.groupids)
@options.add_options(options.templateids)
@options.add_options(options.hostids)
@options.add_options(options.proxyids)
@options.add_options(options.interfaceids)
@options.add_options(options.graphids)
@options.add_options(options.triggerids)
@options.add_options(options.applicationids)
@options.add_options(options.webitems)
@options.add_options(options.inherited)
@options.add_options(options.templated)
@options.add_options(options.monitored)
@options.add_options(options.group)
@options.add_options(options.host)
@options.add_options(options.application)
@options.add_options(options.with_triggers)
@options.add_options(options.selectHosts)
@options.add_options(options.selectInterfaces)
@options.add_options(options.selectTriggers)
@options.add_options(options.selectGraphs)
@options.add_options(options.selectApplications)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectItemDiscovery)
@options.add_options(options.selectPreprocessing)
@options.add_options(options.filter)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['itemid', 'name', 'key_', 'delay', 'history', 'trends', 'type', 'status']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.limit)
@options.add_options(options.nodeids)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def item(zart, sortfield, **kwargs):
    """This command retrieves items."""
    zart.command = 'item'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
