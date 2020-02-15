import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve trends')
@common.add_options(common.itemids)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
@common.add_options(common.countOutput)
@common.add_options(common.limit)
@common.add_options(common.output)
@click.pass_obj
def trend(zart, **kwargs):
    """This command retrieves trends."""
    zart.command = 'trend'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
