import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve autoregistrations')
@options.add_options(options.output)
@click.pass_obj
def autoregistration(zart, **kwargs):
    """This command retrieves autoregistrations."""
    zart.command = 'autoregistration'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
