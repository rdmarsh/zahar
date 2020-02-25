import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve trends')
@options.add_options(options.itemids)
@options.add_options(options.time_from)
@options.add_options(options.time_till)
@options.add_options(options.countOutput)
@options.add_options(options.limit)
@options.add_options(options.output)
@click.pass_obj
def trend(zart, **kwargs):
    """This command retrieves trends."""
    zart.command = 'trend'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
