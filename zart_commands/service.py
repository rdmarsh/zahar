import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve services')
@options.add_options(options.serviceids)
@options.add_options(options.parentids)
@options.add_options(options.childids)
@options.add_options(options.selectParent)
@options.add_options(options.selectDependencies)
@options.add_options(options.selectParentDependencies)
@options.add_options(options.selectTimes)
@options.add_options(options.selectAlarms)
@options.add_options(options.selectTrigger)
@click.option('--sortfield', type=click.Choice(['name', 'sortorder']))
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
def service(zart, sortfield, **kwargs):
    """This command retrieves services."""
    zart.command = 'service'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
