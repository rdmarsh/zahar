import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve triggerprototypes')
@common.add_options(common.active)
@common.add_options(common.applicationids)
@common.add_options(common.discoveryids)
@common.add_options(common.functions)
@common.add_options(common.group)
@common.add_options(common.groupids)
@common.add_options(common.host)
@common.add_options(common.hostids)
@common.add_options(common.inherited)
@common.add_options(common.maintenance)
@common.add_options(common.min_severity)
@common.add_options(common.monitored)
@common.add_options(common.templated)
@common.add_options(common.templateids)
@common.add_options(common.triggerids)
@common.add_options(common.expandExpression)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectDiscoveryRule)
# @common.add_options(common.selectFunctions)
# @common.add_options(common.selectGroups)
# @common.add_options(common.selectHosts)
# @common.add_options(common.selectItems)
# @common.add_options(common.selectDependencies)
# @common.add_options(common.selectTags)
@common.add_options(common.filter)
@common.add_options(common.limitSelects)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['triggerid', 'description', 'status', 'priority']))
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
def triggerprototype(zart, sortfield, **kwargs):
    """This command retrieves triggerprototypes."""
    zart.command = 'triggerprototype'
    engine.engine(zart, sortfield, **kwargs)
