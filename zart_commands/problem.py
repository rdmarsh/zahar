import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve problems')
@options.add_options(options.eventids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.objectids)
@options.add_options(options.applicationids)
@options.add_options(options.source)
@options.add_options(options.object)
@options.add_options(options.acknowledged)
@options.add_options(options.suppressed)
@options.add_options(options.severities)
@options.add_options(options.evaltype)
@options.add_options(options.tags)
@options.add_options(options.recent)
@options.add_options(options.eventid_from)
@options.add_options(options.eventid_till)
@options.add_options(options.time_from)
@options.add_options(options.time_till)
@options.add_options(options.selectAcknowledges)
@options.add_options(options.selectTags)
@options.add_options(options.selectSuppressionData)
@click.option('--sortfield', type=click.Choice(['eventid']))
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
def problem(zart, sortfield, **kwargs):
    """This command retrieves problems."""
    zart.command = 'problem'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
