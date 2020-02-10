import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve templates')
@common.add_options(common.templateids)
@common.add_options(common.groupids)
@common.add_options(common.parentTemplateids)
@common.add_options(common.hostids)
@common.add_options(common.graphids)
@common.add_options(common.itemids)
@common.add_options(common.triggerids)
@common.add_options(common.with_items)
@common.add_options(common.with_triggers)
@common.add_options(common.with_graphs)
@common.add_options(common.with_httptests)
@common.add_options(common.evaltype)
@common.add_options(common.tags)
@common.add_options(common.selectGroups)
@common.add_options(common.selectTags)
@common.add_options(common.selectHosts)
@common.add_options(common.selectTemplates)
@common.add_options(common.selectParentTemplates)
@common.add_options(common.selectHttpTests)
@common.add_options(common.selectItems)
@common.add_options(common.selectDiscoveries)
@common.add_options(common.selectTriggers)
@common.add_options(common.selectGraphs)
@common.add_options(common.selectApplications)
@common.add_options(common.selectMacros)
@common.add_options(common.selectScreens)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
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
def template(zart, sortfield, **kwargs):
    """This command retrieves templates."""
    zart.command = 'template'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
