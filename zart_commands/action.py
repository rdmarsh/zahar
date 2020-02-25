import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve actions')
@options.add_options(options.actionids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.triggerids)
@options.add_options(options.mediatypeids)
@options.add_options(options.usrgrpids)
@options.add_options(options.userids)
@options.add_options(options.scriptids)
@options.add_options(options.selectFilter)
@options.add_options(options.selectConditions)
@options.add_options(options.selectOperations)
@options.add_options(options.selectRecoveryOperations)
@options.add_options(options.selectAcknowledgeOperations)
@click.option('--sortfield', type=click.Choice(['actionid', 'name', 'status']))
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
def action(zart, sortfield, **kwargs):
    """This command retrieves actions."""
    zart.command = 'action'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
