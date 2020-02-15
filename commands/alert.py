import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve alerts')
@common.add_options(common.alertids)
@common.add_options(common.actionids)
@common.add_options(common.eventids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.mediatypeids)
@common.add_options(common.objectids)
@common.add_options(common.userids)
@common.add_options(common.eventobject)
@common.add_options(common.eventsource)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
@common.add_options(common.selectHosts)
@common.add_options(common.selectMediatypes)
@common.add_options(common.selectUsers)
@click.option('--sortfield', type=click.Choice(['alertid', 'clock', 'eventid', 'mediatypeid', 'sendto', 'status']))
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
def alert(zart, sortfield, **kwargs):
    """This command retrieves alerts."""
    zart.command = 'alert'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
