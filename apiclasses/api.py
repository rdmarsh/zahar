import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve apis')
@common.add_options(common.outputformat)
@click.pass_obj
def api(zart, **kwargs):
    """This command retrieves apis."""
    zart.command = 'api'
    engine.engine(zart, **kwargs)
