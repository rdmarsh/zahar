import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve applications')
@options.add_options(options.applicationids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.inherited)
@options.add_options(options.itemids)
@options.add_options(options.templated)
@options.add_options(options.templateids)
@options.add_options(options.expandData)
@options.add_options(options.selectHost)
@options.add_options(options.selectHosts)
@options.add_options(options.selectItems)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectApplicationDiscovery)
@click.option('--sortfield', type=click.Choice(['applicationid', 'name']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
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
def application(zart, sortfield, **kwargs):
    """This command retrieves applications."""
    zart.command = 'application'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
