import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve hostgroups')
@options.add_options(options.graphids)
@options.add_options(options.groupids)
@options.add_options(options.hostids)
@options.add_options(options.maintenanceids)
@options.add_options(options.monitored_hosts)
@options.add_options(options.real_hosts)
@options.add_options(options.templated_hosts)
@options.add_options(options.templateids)
@options.add_options(options.triggerids)
@options.add_options(options.with_applications)
@options.add_options(options.with_graphs)
@options.add_options(options.with_graph_prototypes)
@options.add_options(options.with_hosts_and_templates)
@options.add_options(options.with_httptests)
@options.add_options(options.with_items)
@options.add_options(options.with_item_prototypes)
@options.add_options(options.with_simple_graph_item_prototypes)
@options.add_options(options.with_monitored_httptests)
@options.add_options(options.with_monitored_items)
@options.add_options(options.with_monitored_triggers)
@options.add_options(options.with_simple_graph_items)
@options.add_options(options.with_triggers)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectGroupDiscovery)
@options.add_options(options.selectHosts)
@options.add_options(options.selectTemplates)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['groupid', 'name']))
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
def hostgroup(zart, sortfield, **kwargs):
    """This command retrieves hostgroups."""
    zart.command = 'hostgroup'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
