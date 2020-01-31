import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve hostinterfaces')
@common.add_options(common.hostids)
@common.add_options(common.interfaceids)
@common.add_options(common.itemids)
@common.add_options(common.triggerids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectItems)
# @common.add_options(common.selectHosts)
@common.add_options(common.limitSelects)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['interfaceid', 'dns', 'ip']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.filter)
@common.add_options(common.limit)
# todo: nodeid may be an error in zabbix api doco
@common.add_options(common.nodeids)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def hostinterface(zart, sortfield, **kwargs):
    """This command retrieves hostinterfaces."""
    zart.method = 'hostinterface'
    engine.engine(zart, sortfield, **kwargs)
