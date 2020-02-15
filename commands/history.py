import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve historys')
@options.add_options(options.history)
@options.add_options(options.hostids)
@options.add_options(options.itemids)
@options.add_options(options.time_from)
@options.add_options(options.time_till)
@click.option('--sortfield', type=click.Choice(['itemid', 'clock']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def history(zart, sortfield, **kwargs):
    """This command retrieves historys."""
    zart.command = 'history'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
