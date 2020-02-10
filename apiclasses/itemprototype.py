import logging
import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve itemprototypes')
@common.add_options(common.discoveryids)
@common.add_options(common.graphids)
@common.add_options(common.hostids)
@common.add_options(common.inherited)
@common.add_options(common.itemids)
@common.add_options(common.monitored)
@common.add_options(common.templated)
@common.add_options(common.templateids)
@common.add_options(common.triggerids)
@common.add_options(common.selectApplications)
@common.add_options(common.selectApplicationPrototypes)
@common.add_options(common.selectDiscoveryRule)
@common.add_options(common.selectGraphs)
@common.add_options(common.selectHosts)
@common.add_options(common.selectTriggers)
@common.add_options(common.selectPreprocessing)
@common.add_options(common.filter)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['itemid', 'name', 'key_', 'delay', 'type', 'status']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@click.pass_obj
def itemprototype(zart, sortfield, **kwargs):
    """This command retrieves itemprototypes."""
    zart.command = 'itemprototype'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
