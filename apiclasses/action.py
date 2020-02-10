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
@common.add_options(common.selectFilter)
@common.add_options(common.selectOperations)
@common.add_options(common.selectRecoveryOperations)
@common.add_options(common.selectAcknowledgeOperations)
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
@click.pass_obj
def action(zart, sortfield, **kwargs):
    """This command retrieves actions."""
    zart.command = 'action'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
