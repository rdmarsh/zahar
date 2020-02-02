import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve valuemaps')
@common.add_options(common.valuemapids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectMappings)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['valuemapid', 'name']))
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
def valuemap(zart, sortfield, **kwargs):
    """This command retrieves valuemaps."""
    zart.command = 'valuemap'
    # valuemap command does not fully support sortfield flag
    sortfield=None
    engine.engine(zart, sortfield, **kwargs)
