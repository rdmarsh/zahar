import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve actions')
@common.add_options(common.actionids)
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.triggerids)
@common.add_options(common.mediatypeids)
@common.add_options(common.usrgrpids)
@common.add_options(common.userids)
@common.add_options(common.scriptids)
# todo: for future use once we sort out passing queries
#@common.add_options(common.selectFilters)
#@common.add_options(common.selectOperations)
#@common.add_options(common.selectRecoveryOperations)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['actionid', 'name', 'status']))
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
@common.add_options(common.outputformat)
@click.pass_obj
def action(zart, sortfield, **kwargs):
    """This command retrieves actions."""

# todo: version check placeholder
#    if zart.apiversion == 4 and actionid:
#        actionid=None
#        click.secho('Warning: API Version {} does not support --{} flag,'
#                    ' ignorning'.format(zart.apiversion, 'actionid'),
#                    fg='yellow, err=True)

    #ben magic, throw away False and Empty items
    keywords = {k:v for k,v in kwargs.items() if v}

    # setting the default in common passes a tuple
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = zart.zapi.action.get(**keywords)
    except:
        # todo: fix bare except above and write a better error messages
        click.secho('Error: todo.',
                    fg='red', err=True)

    if 'countOutput' in keywords and keywords['countOutput']:
        click.echo(obj)
    else:
        outputformat.outputformat(obj, keywords['outputformat'])

    if 'limit' in keywords and len(obj) >= keywords['limit']:
        click.secho('Warning: row limit matches records returned,'
                    ' there may be data you are not seeing.',
                    fg='yellow', err=True)
