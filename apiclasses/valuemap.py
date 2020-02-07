import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve valuemaps')
@common.add_options(common.valuemapids)
@common.add_options(common.selectMappings)
@click.option('--sortfield', type=click.Choice(['valuemapid']))
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
def valuemap(zart, sortfield, **kwargs):
    """This command retrieves valuemaps."""
    zart.command = 'valuemap'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
