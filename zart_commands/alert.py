import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve alerts')
@options.add_options(options.alertids)
@options.add_options(options.actionids)
@options.add_options(options.eventids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.mediatypeids)
@options.add_options(options.triggerids)
@options.add_options(options.objectids)
@options.add_options(options.userids)
@options.add_options(options.eventobject)
@options.add_options(options.eventsource)
@options.add_options(options.time_from)
@options.add_options(options.time_till)
@options.add_options(options.selectHosts)
@options.add_options(options.selectMediatypes)
@options.add_options(options.selectUsers)
@click.option('--sortfield', type=click.Choice(['alertid', 'clock', 'eventid', 'mediatypeid', 'sendto', 'status']))
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
def alert(zart, sortfield, **kwargs):
    """This command retrieves alerts."""
    zart.command = 'alert'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
