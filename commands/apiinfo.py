import logging
import click
import engine


@click.command(short_help='retrieve apiinfos')
@click.pass_obj
def apiinfo(zart, **kwargs):
    """This command retrieves apiinfos."""
    zart.command = 'apiinfo'
    logging.debug('zart.command: %s', zart.command)
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
