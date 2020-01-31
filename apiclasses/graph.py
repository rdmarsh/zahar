import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve graphs')
@common.add_options(common.graphids)
@common.add_options(common.groupids)
@common.add_options(common.templateids)
@common.add_options(common.hostids)
@common.add_options(common.itemids)
@common.add_options(common.templated)
@common.add_options(common.inherited)
@common.add_options(common.expandName)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectGroups)
# @common.add_options(common.selectTemplates)
# @common.add_options(common.selectHosts)
# @common.add_options(common.selectItems)
# @common.add_options(common.selectGraphDiscovery)
# @common.add_options(common.selectGraphItems)
# @common.add_options(common.selectDiscoveryRule)
@common.add_options(common.filter)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['graphid', 'name', 'graphtype']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
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
def graph(zart, sortfield, **kwargs):
    """This command retrieves graphs."""
    zart.method = 'graph'
    engine.engine(zart, sortfield, **kwargs)
