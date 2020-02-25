import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve mediatypes')
@options.add_options(options.mediatypeids)
@options.add_options(options.mediaids)
@options.add_options(options.userids)
@options.add_options(options.selectMessageTemplates)
@options.add_options(options.selectUsers)
@click.option('--sortfield', type=click.Choice(['mediatypeid']))
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
def mediatype(zart, sortfield, **kwargs):
    """This command retrieves mediatypes."""
    zart.command = 'mediatype'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
