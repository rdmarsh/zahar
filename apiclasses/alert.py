import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve alerts')
@common.add_options(common.alertids)
@common.add_options(common.actionids)
@common.add_options(common.eventids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.mediatypeids)
@common.add_options(common.objectids)
@common.add_options(common.userids)
# todo: fix the way integer works for these
# @common.add_options(common.eventobject)
# @common.add_options(common.eventsource)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectHosts)
# @common.add_options(common.selectMediatypes)
# @common.add_options(common.selectUsers)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['alertid', 'clock', 'eventid', 'status']))
@common.add_options(common.countOutput)
# @common.add_options(common.editable)
# @common.add_options(common.excludeSearch)
# @common.add_options(common.filter)
@common.add_options(common.limit)
# @common.add_options(common.output)
# @common.add_options(common.preservekeys)
# @common.add_options(common.search)
# @common.add_options(common.searchByAny)
# @common.add_options(common.searchWildcardsEnabled)
# @common.add_options(common.sortorder)
# @common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def alert(zart, sortfield, **kwargs):
    """This command retrieves alerts."""
    zart.method = 'alert'
    engine.engine(zart, sortfield, **kwargs)
