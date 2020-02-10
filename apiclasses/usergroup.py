import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve usergroups')
@common.add_options(common.status)
@common.add_options(common.userids)
@common.add_options(common.usrgrpids)
@common.add_options(common.with_gui_access)
@common.add_options(common.selectTagFilters)
@common.add_options(common.selectUsers)
@common.add_options(common.selectRights)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['usrgrpid', 'name']))
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
def usergroup(zart, sortfield, **kwargs):
    """This command retrieves usergroups."""
    zart.command = 'usergroup'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
