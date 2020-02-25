import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve graphs')
@options.add_options(options.graphids)
@options.add_options(options.groupids)
@options.add_options(options.templateids)
@options.add_options(options.hostids)
@options.add_options(options.itemids)
@options.add_options(options.templated)
@options.add_options(options.inherited)
@options.add_options(options.expandName)
@options.add_options(options.selectGroups)
@options.add_options(options.selectTemplates)
@options.add_options(options.selectHosts)
@options.add_options(options.selectItems)
@options.add_options(options.selectGraphDiscovery)
@options.add_options(options.selectGraphItems)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.filter)
@click.option('--sortfield', type=click.Choice(['graphid', 'name', 'graphtype']))
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
def graph(zart, sortfield, **kwargs):
    """This command retrieves graphs."""
    zart.command = 'graph'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
