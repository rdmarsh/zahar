import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve triggerprototypes')
@options.add_options(options.active)
@options.add_options(options.applicationids)
@options.add_options(options.discoveryids)
@options.add_options(options.functions)
@options.add_options(options.group)
@options.add_options(options.groupids)
@options.add_options(options.host)
@options.add_options(options.hostids)
@options.add_options(options.inherited)
@options.add_options(options.maintenance)
@options.add_options(options.min_severity)
@options.add_options(options.monitored)
@options.add_options(options.templated)
@options.add_options(options.templateids)
@options.add_options(options.triggerids)
@options.add_options(options.expandExpression)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectFunctions)
@options.add_options(options.selectGroups)
@options.add_options(options.selectHosts)
@options.add_options(options.selectItems)
@options.add_options(options.selectDependencies)
@options.add_options(options.selectTags)
@options.add_options(options.filter)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['triggerid', 'description', 'status', 'priority']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def triggerprototype(zart, sortfield, **kwargs):
    """This command retrieves triggerprototypes."""
    zart.command = 'triggerprototype'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
