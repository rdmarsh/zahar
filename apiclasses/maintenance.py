import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve maintenances')
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.maintenanceids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectGroups)
# @common.add_options(common.selectHosts)
# @common.add_options(common.selectTimeperiods)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['maintenanceid', 'name', 'maintenance_type']))
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
def maintenance(zart, sortfield, **kwargs):
    """This command retrieves maintenances."""
    zart.method = 'maintenance'
    engine.engine(zart, sortfield, **kwargs)
