import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve usergroups')
@options.add_options(options.status)
@options.add_options(options.userids)
@options.add_options(options.usrgrpids)
@options.add_options(options.with_gui_access)
@options.add_options(options.selectTagFilters)
@options.add_options(options.selectUsers)
@options.add_options(options.selectRights)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['usrgrpid', 'name']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
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
