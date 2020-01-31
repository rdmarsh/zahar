import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve users')
@common.add_options(common.mediaids)
@common.add_options(common.mediatypeids)
@common.add_options(common.userids)
@common.add_options(common.usrgrpids)
@common.add_options(common.getAccess)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectMedias)
# @common.add_options(common.selectMediatypes)
# @common.add_options(common.selectUsrgrps)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['userid', 'alias']))
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
def user(zart, sortfield, **kwargs):
    """This command retrieves users."""
    zart.method = 'user'
    engine.engine(zart, sortfield, **kwargs)
