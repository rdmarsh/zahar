import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve drules')
@common.add_options(common.dhostids)
@common.add_options(common.druleids)
@common.add_options(common.dserviceids)
# todo: for future use once we sort out passing queries
#@common.add_options(common.selectDChecks)
#@common.add_options(common.selectDHosts)
@common.add_options(common.limitSelects)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['druleid', 'name']))
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
def drule(zart, sortfield, **kwargs):
    """This command retrieves drules."""

# todo: make better
    keywords = {}
    for option in [
            'dhostids',
            'druleids',
            'dserviceids',
            'selectDChecks',
            'selectDHosts',
            'limitSelects',
            #'sortfield',
            'countOutput',
            'editable',
            'excludeSearch',
            'filter',
            'limit',
            'output',
            'preservekeys',
            'search',
            'searchByAny',
            'searchWildcardsEnabled',
            'sortorder',
            'startSearch',
            'outputformat',
            ]:
        keywords[option] = kwargs.get(option) if kwargs.get(option) else None

    # setting the default in common passes a tuple
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = zart.zapi.drule.get(**keywords)
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
