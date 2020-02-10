import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve serviceslas')
@common.add_options(common.serviceids)
@common.add_options(common.intervals_from)
@common.add_options(common.intervals_to)
@click.pass_obj
def servicesla(zart, **kwargs):
    """This command retrieves serviceslas."""
    zart.command = 'servicesla'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
