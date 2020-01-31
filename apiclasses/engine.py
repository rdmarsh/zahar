import click
import pandas as pd


def engine(zart, sortfield, **kwargs):
    """This is common engine for all commands."""

    # ben magic, throw away False and Empty items
    keywords = {k:v for k,v in kwargs.items() if v}

    # setting the default in common passes a tuple
    # maybe there's a better way?
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common flags
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = getattr(zart.zapi, zart.method).get(**keywords)
        # obj = zart.zapi.image.get(**keywords)
    except:
        # todo: fix bare except above and write a better error messages
        click.secho('Error: todo.',
                    fg='red', err=True)

    if 'countOutput' in keywords and keywords['countOutput']:
        if type(obj) is int:
            click.echo(obj)
        else:
            click.secho('0', fg='yellow')
            click.secho('Warning: no values returned,'
                        ' assuming 0 or this flag is not supported.',
                        fg='yellow', err=True)
    else:
        outputformat(obj, keywords['outputformat'])

        if 'limit' in keywords and len(obj) >= keywords['limit']:
            click.secho('Warning: row limit matches records returned,'
                        ' there may be data you are not seeing.',
                        fg='yellow', err=True)


def outputformat(obj, outputformat='txt'):
    df = pd.DataFrame(obj)

    if not df.empty:
        if outputformat == 'csv':
            click.echo(df.to_csv(index=False))
        elif outputformat == 'html':
            click.echo(df.to_html(index=False))
        elif outputformat == 'json':
            click.echo(df.to_json(orient='records'))
        elif outputformat == 'latex':
            click.echo(df.to_latex(index=False))
        elif outputformat == 'raw':
            click.echo(obj)
        elif outputformat == 'clip':
            click.echo(df.to_clipboard(index=False))
        elif outputformat == 'xls':
            # click.echo("df.to_excel(index=False)")
            click.secho('Info: xls outputformat will be added in future',
                        fg='green', err=True)
        else:
            # default to txt
            click.echo(df.to_string(index=False,))
    else:
        click.secho('Warning: no data found', fg='yellow', err=True)

def version_check():
    # todo: placeholder
    # api version parameter checks
    # parm_ver = {}
    # parm_ver['dependent'] = 4.2
    # parm_ver['evaltype'] = 4.0

    # for parm in parm_ver:
    #     if parm in keywords and keywords[parm] and zart.apiversion < parm_ver[parm]:
    #         keywords[parm]=None
    #         click.secho('Warning: API Version {:.1f} does not support "--{}" flag,'
    #                     ' ignorning'.format(zart.apiversion, parm),
    #                     fg='yellow', err=True)
    return

