import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve drules')
@common.add_options(common.dhostids)
@common.add_options(common.druleids)
@common.add_options(common.dserviceids)
@common.add_options(common.selectDChecks)
@common.add_options(common.selectDHosts)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['druleid', 'name']))
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
def drule(zart, sortfield, **kwargs):
    """This command retrieves drules."""
    zart.command = 'drule'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
