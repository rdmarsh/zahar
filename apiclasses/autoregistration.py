import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve autoregistrations')
@common.add_options(common.output)
@click.pass_obj
def autoregistration(zart, **kwargs):
    """This command retrieves autoregistrations."""
    zart.command = 'autoregistration'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
