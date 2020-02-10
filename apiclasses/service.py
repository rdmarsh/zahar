import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve services')
@common.add_options(common.serviceids)
@common.add_options(common.parentids)
@common.add_options(common.childids)
@common.add_options(common.selectParent)
@common.add_options(common.selectDependencies)
@common.add_options(common.selectParentDependencies)
@common.add_options(common.selectTimes)
@common.add_options(common.selectAlarms)
@common.add_options(common.selectTrigger)
@click.option('--sortfield', type=click.Choice(['name', 'sortorder']))
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
def service(zart, sortfield, **kwargs):
    """This command retrieves services."""
    zart.command = 'service'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
