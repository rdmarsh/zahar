import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve graphitems')
@common.add_options(common.gitemids)
@common.add_options(common.graphids)
@common.add_options(common.itemids)
@common.add_options(common.type)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectGraphs)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['gitemid']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.sortorder)
@common.add_options(common.outputformat)
@click.pass_obj
def graphitem(zart, sortfield, **kwargs):
    """This command retrieves graphitems."""
    zart.method = 'graphitem'
    engine.engine(zart, sortfield, **kwargs)
