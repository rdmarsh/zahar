import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve serviceslas')
@common.add_options(common.serviceids)
@common.add_options(common.interval_from)
@common.add_options(common.interval_to)
@click.pass_obj
def servicesla(zart, **kwargs):
    """This command retrieves serviceslas."""
    zart.command = 'servicesla'
    engine.engine(zart, **kwargs)
