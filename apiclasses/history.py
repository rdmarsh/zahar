import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve historys')
@common.add_options(common.history)
@common.add_options(common.hostids)
@common.add_options(common.itemids)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['itemid', 'clock']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.filter)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def history(zart, sortfield, **kwargs):
    """This command retrieves historys."""
    zart.method = 'history'
    engine.engine(zart, sortfield, **kwargs)
