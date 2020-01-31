import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve actions')
@common.add_options(common.actionids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.triggerids)
@common.add_options(common.mediatypeids)
@common.add_options(common.usrgrpids)
@common.add_options(common.userids)
@common.add_options(common.scriptids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectFilters)
# @common.add_options(common.selectOperations)
# @common.add_options(common.selectRecoveryOperations)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['actionid', 'name', 'status']))
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
def action(zart, sortfield, **kwargs):
    """This command retrieves actions."""
    zart.method = 'action'
    engine.engine(zart, sortfield, **kwargs)
