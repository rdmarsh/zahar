import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve serviceslas')
@options.add_options(options.serviceids)
@options.add_options(options.intervals_from)
@options.add_options(options.intervals_to)
@click.pass_obj
def servicesla(zart, **kwargs):
    """This command retrieves serviceslas."""
    zart.command = 'servicesla'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
