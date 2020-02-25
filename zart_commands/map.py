import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve maps')
@options.add_options(options.sysmapids)
@options.add_options(options.userids)
@options.add_options(options.expandUrls)
@options.add_options(options.selectIconMap)
@options.add_options(options.selectLinks)
@options.add_options(options.selectSelements)
@options.add_options(options.selectUrls)
@options.add_options(options.selectUsers)
@options.add_options(options.selectUserGroups)
@options.add_options(options.selectShapes)
@options.add_options(options.selectLines)
@click.option('--sortfield', type=click.Choice(['name', 'width', 'height']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
@options.add_options(options.limit)
@options.add_options(options.nodeids)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def map(zart, sortfield, **kwargs):
    """This command retrieves maps."""
    zart.command = 'map'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
