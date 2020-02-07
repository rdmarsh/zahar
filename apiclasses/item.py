import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve items')
@common.add_options(common.itemids)
@common.add_options(common.groupids)
@common.add_options(common.templateids)
@common.add_options(common.hostids)
@common.add_options(common.proxyids)
@common.add_options(common.interfaceids)
@common.add_options(common.graphids)
@common.add_options(common.triggerids)
@common.add_options(common.applicationids)
@common.add_options(common.webitems)
@common.add_options(common.inherited)
@common.add_options(common.templated)
@common.add_options(common.monitored)
@common.add_options(common.group)
@common.add_options(common.host)
@common.add_options(common.application)
@common.add_options(common.with_triggers)
@common.add_options(common.selectHosts)
@common.add_options(common.selectInterfaces)
@common.add_options(common.selectTriggers)
@common.add_options(common.selectGraphs)
@common.add_options(common.selectApplications)
@common.add_options(common.selectDiscoveryRule)
@common.add_options(common.selectItemDiscovery)
@common.add_options(common.selectPreprocessing)
@common.add_options(common.filter)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['itemid', 'name', 'key_', 'delay', 'history', 'trends', 'type', 'status']))
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
def item(zart, sortfield, **kwargs):
    """This command retrieves items."""
    zart.command = 'item'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
