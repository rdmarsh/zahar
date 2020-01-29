import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve dchecks')
@common.add_options(common.dcheckids)
@common.add_options(common.druleids)
@common.add_options(common.dserviceids)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['dcheckid', 'druleid']))
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
def dcheck(zart, sortfield, **kwargs):
    """This command retrieves dchecks."""

# todo: make better
    keywords = {}
    for option in [
            'dcheckids',
            'druleids',
            'dserviceids',
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
        obj = zart.zapi.dcheck.get(**keywords)
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
