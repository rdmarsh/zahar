import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve auditlogs')
@options.add_options(options.auditids)
@options.add_options(options.userids)
@options.add_options(options.time_from)
@options.add_options(options.time_till)
@options.add_options(options.selectDetails)
@click.option('--sortfield', type=click.Choice(['auditid', 'userid', 'clock']))
@options.add_options(options.filter)
@options.add_options(options.search)
@options.add_options(options.countOutput)
@options.add_options(options.excludeSearch)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def auditlog(zart, sortfield, **kwargs):
    """This command retrieves auditlogs."""
    zart.command = 'auditlog'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
