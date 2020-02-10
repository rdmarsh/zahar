import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve graphprototypes')
@common.add_options(common.discoveryids)
@common.add_options(common.graphids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.inherited)
@common.add_options(common.itemids)
@common.add_options(common.templated)
@common.add_options(common.templateids)
@common.add_options(common.selectDiscoveryRule)
@common.add_options(common.selectGraphItems)
@common.add_options(common.selectGroups)
@common.add_options(common.selectHosts)
@common.add_options(common.selectItems)
@common.add_options(common.selectTemplates)
@common.add_options(common.filter)
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
@click.pass_obj
def graphprototype(zart, sortfield, **kwargs):
    """This command retrieves graphprototypes."""
    zart.command = 'graphprototype'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
