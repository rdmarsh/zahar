import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve httptests')
@common.add_options(common.applicationids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.httptestids)
@common.add_options(common.inherited)
@common.add_options(common.monitored)
@common.add_options(common.templated)
@common.add_options(common.templateids)
@common.add_options(common.expandName)
@common.add_options(common.expandStepName)
@common.add_options(common.selectHosts)
@common.add_options(common.selectSteps)
@click.option('--sortfield', type=click.Choice(['httptestid', 'name']))
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
def httptest(zart, sortfield, **kwargs):
    """This command retrieves httptests."""
    zart.command = 'httptest'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
