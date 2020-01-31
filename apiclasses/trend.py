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
@common.add_options(common.outputformat)
@click.pass_obj
def trend(zart, **kwargs):
    """This command retrieves trends."""
    zart.method = 'trend'
    sortfield=None
    engine.engine(zart, sortfield, **kwargs)
