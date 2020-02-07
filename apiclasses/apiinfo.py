import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve apiinfos')
@click.pass_obj
def apiinfo(zart, **kwargs):
    """This command retrieves apiinfos."""
    zart.command = 'apiinfo'
    engine.engine(zart, **kwargs)
