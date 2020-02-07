import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve dashboards')
@common.add_options(common.dashboardids)
@common.add_options(common.selectWidgets)
@common.add_options(common.selectUsers)
@common.add_options(common.selectUserGroups)
@click.option('--sortfield', type=click.Choice(['dashboardid']))
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
def dashboard(zart, sortfield, **kwargs):
    """This command retrieves dashboards."""
    zart.command = 'dashboard'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
