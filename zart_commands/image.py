import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve images')
@options.add_options(options.imageids)
@options.add_options(options.sysmapids)
@options.add_options(options.select_image)
@click.option('--sortfield', type=click.Choice(['imageid', 'name']))
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
def image(zart, sortfield, **kwargs):
    """This command retrieves images."""
    zart.command = 'image'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
