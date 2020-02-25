import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve usermacros')
@options.add_options(options.globalmacro)
@options.add_options(options.globalmacroids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.hostmacroids)
@options.add_options(options.templateids)
@options.add_options(options.selectGroups)
@options.add_options(options.selectHosts)
@options.add_options(options.selectTemplates)
@click.option('--sortfield', type=click.Choice(['macro']))
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
def usermacro(zart, sortfield, **kwargs):
    """This command retrieves usermacros."""
    zart.command = 'usermacro'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
