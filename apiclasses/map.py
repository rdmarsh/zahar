import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve maps')
@common.add_options(common.sysmapids)
@common.add_options(common.userids)
@common.add_options(common.expandUrls)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectIconMap)
# @common.add_options(common.selectLinks)
# @common.add_options(common.selectSelements)
# @common.add_options(common.selectUrls)
# @common.add_options(common.selectUsers)
# @common.add_options(common.selectUserGroups)
# @common.add_options(common.selectShapes)
# @common.add_options(common.selectLines)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['name', 'width', 'height']))
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
def map(zart, sortfield, **kwargs):
    """This command retrieves maps."""
    zart.command = 'map'
    engine.engine(zart, sortfield, **kwargs)
