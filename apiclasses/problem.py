import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve problems')
@common.add_options(common.eventids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.objectids)
@common.add_options(common.applicationids)
@common.add_options(common.source)
@common.add_options(common.object)
@common.add_options(common.acknowledged)
@common.add_options(common.severities)
@common.add_options(common.tags)
@common.add_options(common.recent)
@common.add_options(common.eventid_from)
@common.add_options(common.eventid_till)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectAcknowledges)
# @common.add_options(common.selectTags)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['eventid']))
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
def problem(zart, sortfield, **kwargs):
    """This command retrieves problems."""
    zart.command = 'problem'
    engine.engine(zart, sortfield, **kwargs)
