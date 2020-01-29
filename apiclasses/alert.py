import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve alerts')
@common.add_options(common.alertids)
@common.add_options(common.actionids)
@common.add_options(common.eventids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.mediatypeids)
@common.add_options(common.objectids)
@common.add_options(common.userids)
# todo: fix the way integer works for these
#@common.add_options(common.eventobject)
#@common.add_options(common.eventsource)
@common.add_options(common.time_from)
@common.add_options(common.time_till)
## todo: for future use once we sort out passing queries
##@common.add_options(common.selectHosts)
##@common.add_options(common.selectMediatypes)
##@common.add_options(common.selectUsers)
## todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['alertid', 'clock', 'eventid', 'status']))
@common.add_options(common.countOutput)
#@common.add_options(common.editable)
#@common.add_options(common.excludeSearch)
#@common.add_options(common.filter)
@common.add_options(common.limit)
#@common.add_options(common.output)
#@common.add_options(common.preservekeys)
#@common.add_options(common.search)
#@common.add_options(common.searchByAny)
#@common.add_options(common.searchWildcardsEnabled)
#@common.add_options(common.sortorder)
#@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def alert(zart, sortfield, **kwargs):
    """This command retrieves alerts."""

# todo: make better
    keywords = {}
    for option in [
            'alertids',
            'actionids',
            'eventids',
            'groupids',
            'hostids',
            'mediatypeids',
            'objectids',
            'userids',
            #'eventobject',
            #'eventsource',
            'time_from',
            'time_till',
            #'selectHosts',
            #'selectMediatypes',
            #'selectUsers',
            #'sortfield',
            'countOutput',
            #'editable',
            #'excludeSearch',
            #'filter',
            'limit',
            #'output',
            #'preservekeys',
            #'search',
            #'searchByAny',
            #'searchWildcardsEnabled',
            #'sortorder',
            #'startSearch',
            'outputformat',
            ]:
        keywords[option] = kwargs.get(option) if kwargs.get(option) else None

    # setting the default in common passes a tuple
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = zart.zapi.alert.get(**keywords)
    except:
        # todo: fix bare except above and write a better error messages
        click.secho('Error: todo.',
                    fg='red', err=True)

    if keywords['countOutput'] is None:
        outputformat.outputformat(obj, keywords['outputformat'])
    else:
        click.echo(obj)

    if keywords['limit'] and len(obj) >= keywords['limit']:
        click.secho('Warning: row limit matches records returned,'
                    ' there may be data you are not seeing.',
                    fg='yellow', err=True)
