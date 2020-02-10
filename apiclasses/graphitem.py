import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve graphitems')
@common.add_options(common.gitemids)
@common.add_options(common.graphids)
@common.add_options(common.itemids)
@common.add_options(common.type)
@common.add_options(common.selectGraphs)
@click.option('--sortfield', type=click.Choice(['gitemid']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.sortorder)
@click.pass_obj
def graphitem(zart, sortfield, **kwargs):
    """This command retrieves graphitems."""
    zart.command = 'graphitem'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
