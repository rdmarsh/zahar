import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve dashboards')
@options.add_options(options.dashboardids)
@options.add_options(options.selectWidgets)
@options.add_options(options.selectUsers)
@options.add_options(options.selectUserGroups)
@click.option('--sortfield', type=click.Choice(['dashboardid']))
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
def dashboard(zart, sortfield, **kwargs):
    """This command retrieves dashboards."""
    zart.command = 'dashboard'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
