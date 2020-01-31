import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve applications')
@common.add_options(common.applicationids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.inherited)
@common.add_options(common.itemids)
@common.add_options(common.templated)
@common.add_options(common.templateids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectHost)
# @common.add_options(common.selectItems)
# @common.add_options(common.selectDiscoveryRule)
# @common.add_options(common.selectApplicationDiscovery)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['applicationid', 'name']))
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
def application(zart, sortfield, **kwargs):
    """This command retrieves applications."""
    zart.method = 'application'
    engine.engine(zart, sortfield, **kwargs)
