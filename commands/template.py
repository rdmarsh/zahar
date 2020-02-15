import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve templates')
@options.add_options(options.templateids)
@options.add_options(options.groupids)
@options.add_options(options.parentTemplateids)
@options.add_options(options.hostids)
@options.add_options(options.graphids)
@options.add_options(options.itemids)
@options.add_options(options.triggerids)
@options.add_options(options.with_items)
@options.add_options(options.with_triggers)
@options.add_options(options.with_graphs)
@options.add_options(options.with_httptests)
@options.add_options(options.evaltype)
@options.add_options(options.tags)
@options.add_options(options.selectGroups)
@options.add_options(options.selectTags)
@options.add_options(options.selectHosts)
@options.add_options(options.selectTemplates)
@options.add_options(options.selectParentTemplates)
@options.add_options(options.selectHttpTests)
@options.add_options(options.selectItems)
@options.add_options(options.selectDiscoveries)
@options.add_options(options.selectTriggers)
@options.add_options(options.selectGraphs)
@options.add_options(options.selectApplications)
@options.add_options(options.selectMacros)
@options.add_options(options.selectScreens)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
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
def template(zart, sortfield, **kwargs):
    """This command retrieves templates."""
    zart.command = 'template'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
