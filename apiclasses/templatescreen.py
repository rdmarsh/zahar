import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve templatescreens')
@common.add_options(common.hostids)
@common.add_options(common.screenids)
@common.add_options(common.screenitemids)
@common.add_options(common.templateids)
@common.add_options(common.noInheritance)
@common.add_options(common.selectScreenItems)
@click.option('--sortfield', type=click.Choice(['screenid', 'name']))
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
def templatescreen(zart, sortfield, **kwargs):
    """This command retrieves templatescreens."""
    zart.command = 'templatescreen'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
