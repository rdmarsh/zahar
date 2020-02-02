import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve screenitems')
@common.add_options(common.screenitemids)
@common.add_options(common.screenids)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['screenitemid', 'screenid']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.filter)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def screenitem(zart, sortfield, **kwargs):
    """This command retrieves screenitems."""
    zart.command = 'screenitem'
    engine.engine(zart, sortfield, **kwargs)
