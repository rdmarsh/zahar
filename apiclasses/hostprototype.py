import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve hostprototypes')
@common.add_options(common.hostids)
@common.add_options(common.discoveryids)
@common.add_options(common.inherited)
@common.add_options(common.selectDiscoveryRule)
@common.add_options(common.selectGroupLinks)
@common.add_options(common.selectGroupPrototypes)
@common.add_options(common.selectInventory)
@common.add_options(common.selectParentHost)
@common.add_options(common.selectTemplates)
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
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
def hostprototype(zart, sortfield, **kwargs):
    """This command retrieves hostprototypes."""
    zart.command = 'hostprototype'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
