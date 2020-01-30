import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve hostprototypes')
@common.add_options(common.hostids)
@common.add_options(common.discoveryids)
@common.add_options(common.inherited)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectDiscoveryRule)
# @common.add_options(common.selectGroupLinks)
# @common.add_options(common.selectGroupPrototypes)
# @common.add_options(common.selectInventory)
# @common.add_options(common.selectParentHost)
# @common.add_options(common.selectTemplates)
# todo: work out how to pass choices to DRY this
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
@common.add_options(common.outputformat)
@click.pass_obj
def hostprototype(zart, sortfield, **kwargs):
    """This command retrieves hostprototypes."""

    #ben magic, throw away False and Empty items
    keywords = {k:v for k,v in kwargs.items() if v}

    # setting the default in common passes a tuple
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = zart.zapi.hostprototype.get(**keywords)
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
