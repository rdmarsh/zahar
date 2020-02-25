import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve hostprototypes')
@options.add_options(options.hostids)
@options.add_options(options.discoveryids)
@options.add_options(options.inherited)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectGroupLinks)
@options.add_options(options.selectGroupPrototypes)
@options.add_options(options.selectInventory)
@options.add_options(options.selectParentHost)
@options.add_options(options.selectTemplates)
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def hostprototype(zart, sortfield, **kwargs):
    """This command retrieves hostprototypes."""
    zart.command = 'hostprototype'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
