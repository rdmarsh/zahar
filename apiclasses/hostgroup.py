import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve hostgroups')
@common.add_options(common.graphids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.maintenanceids)
@common.add_options(common.monitored_hosts)
@common.add_options(common.real_hosts)
@common.add_options(common.templated_hosts)
@common.add_options(common.templateids)
@common.add_options(common.triggerids)
@common.add_options(common.with_applications)
@common.add_options(common.with_graphs)
@common.add_options(common.with_hosts_and_templates)
@common.add_options(common.with_httptests)
@common.add_options(common.with_items)
@common.add_options(common.with_monitored_httptests)
@common.add_options(common.with_monitored_items)
@common.add_options(common.with_monitored_triggers)
@common.add_options(common.with_simple_graph_items)
@common.add_options(common.with_triggers)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectDiscoveryRule)
# @common.add_options(common.selectGroupDiscovery)
# @common.add_options(common.selectHosts)
# @common.add_options(common.selectTemplates)
@common.add_options(common.limitSelects)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['groupid', 'name']))
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
def hostgroup(zart, sortfield, **kwargs):
    """This command retrieves hostgroups."""
    zart.command = 'hostgroup'
    engine.engine(zart, sortfield, **kwargs)
