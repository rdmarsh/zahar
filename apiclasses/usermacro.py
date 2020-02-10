import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve usermacros')
@common.add_options(common.globalmacro)
@common.add_options(common.globalmacroids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.hostmacroids)
@common.add_options(common.templateids)
@common.add_options(common.selectGroups)
@common.add_options(common.selectHosts)
@common.add_options(common.selectTemplates)
@click.option('--sortfield', type=click.Choice(['macro']))
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
def usermacro(zart, sortfield, **kwargs):
    """This command retrieves usermacros."""
    zart.command = 'usermacro'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
