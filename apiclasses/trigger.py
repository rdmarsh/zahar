import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve triggers')
@common.add_options(common.triggerids)
@common.add_options(common.groupids)
@common.add_options(common.templateids)
@common.add_options(common.hostids)
@common.add_options(common.itemids)
@common.add_options(common.applicationids)
@common.add_options(common.functions)
@common.add_options(common.group)
@common.add_options(common.host)
@common.add_options(common.inherited)
@common.add_options(common.templated)
@common.add_options(common.dependent)
@common.add_options(common.monitored)
@common.add_options(common.active)
@common.add_options(common.maintenance)
@common.add_options(common.withUnacknowledgedEvents)
@common.add_options(common.withAcknowledgedEvents)
@common.add_options(common.withLastEventUnacknowledged)
@common.add_options(common.skipDependent)
@common.add_options(common.lastChangeSince)
@common.add_options(common.lastChangeTill)
@common.add_options(common.only_true)
@common.add_options(common.min_severity)
@common.add_options(common.evaltype)
@common.add_options(common.tags)
@common.add_options(common.expandComment)
@common.add_options(common.expandDescription)
@common.add_options(common.expandExpression)
@common.add_options(common.selectGroups)
@common.add_options(common.selectHosts)
@common.add_options(common.selectItems)
@common.add_options(common.selectFunctions)
@common.add_options(common.selectDependencies)
@common.add_options(common.selectDiscoveryRule)
@common.add_options(common.selectLastEvent)
@common.add_options(common.selectTags)
@common.add_options(common.selectTriggerDiscovery)
@common.add_options(common.filter)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['triggerid', 'description', 'status', 'priority', 'lastchange', 'hostname']))
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
@common.add_options(common.outputformat)
@click.pass_obj
def trigger(zart, sortfield, **kwargs):
    """This command retrieves triggers."""
    zart.command = 'trigger'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
