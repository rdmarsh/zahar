import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve images')
@common.add_options(common.imageids)
@common.add_options(common.sysmapids)
@common.add_options(common.select_image)
@click.option('--sortfield', type=click.Choice(['imageid', 'name']))
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
def image(zart, sortfield, **kwargs):
    """This command retrieves images."""
    zart.command = 'image'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
