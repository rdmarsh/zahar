import click
import pandas as pd
from packaging import version


def engine(zart, **kwargs):
    """This is common engine for all commands."""

    # ben magic, throw away False and Empty flags
    flags = {k: v for k, v in kwargs.items() if v}

    # setting the default in common passes a tuple
    # maybe there's a better way?
    #if kwargs.get('output') and 'extend' in kwargs.get('output'):
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        flags['output'] = 'extend'

    # at the moment it's all or nothing, maybe in future
    # we can change this and select what we want returned
    for select in [
            'selectAcknowledgeOperations',
            'selectApplicationDiscovery',
            'selectApplications',
            'selectDiscoveries',
            'selectDiscoveryRule',
            'selectFilter',
            'selectGraphs',
            'selectGroups',
            'selectHost',
            'selectHosts',
            'selectItems',
            'selectMediatypes',
            'selectOperations',
            'selectRecoveryOperations',
            'selectUserGroups',
            'selectUsers',
            'selectWidgets',
            ]:
        if kwargs.get(select):
            flags[select] = 'extend'

    # version checks
    version_check(zart.apiv, zart.command, flags.keys())

    if zart.command == 'history' or zart.command == 'valuemap':
        # probably not needed: del flags['sortfield']
        #click.secho(zart.command + ' doesnt support sortmap', bg='red', fg='white', err=True)
        try:
            obj = getattr(zart.zapi, zart.command).get(limit=1)
        except:
            # todo: fix bare except above and write a better error messages
            click.secho('Error: todo Exception.',
                        fg='red', err=True)
    else:

        try:
            obj = getattr(zart.zapi, zart.command).get(**flags)
        except:
            # todo: fix bare except above and write a better error messages
            click.secho('Error: todo Exception.',
                        fg='red', err=True)

    if 'countOutput' in flags and flags['countOutput']:
        if str(obj).isdigit():
            click.echo(obj)
        else:
            click.secho('0', fg='yellow')
            click.secho('Warning: no values returned,'
                        ' assuming 0 or this flag is not supported.',
                        fg='yellow', err=True)
    else:
        outputformat(obj, flags['outputformat'])

        if 'limit' in flags and len(obj) >= flags['limit']:
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


def version_check(apiv, command, flags):
    # todo: convert into a json object we can load
    version_dict = {
            'autoregistration': {
                '*': ('4.4', '99'),
                },
            'dashboard': {
                '*': ('99', '99'),
                },
            'usermedia': {
                '*': ('2.0', '3.4'),
                },
            'history': {
                '*': ('99', '99'),
                },
            'trigger': {
                'dependent': ('4.2', '99'),
                'evaltype': ('4.0', '99'),
                },
            }

    if command in version_dict:
        if '*' in version_dict[command]:
            #if not version_dict[command]['*'][0] <= apiv <= version_dict[command]['*'][1]:
            if not version.parse(version_dict[command]['*'][0]) <= version.parse(apiv) <= version.parse(version_dict[command]['*'][1]):
                click.secho('Error: API Version {} does not support the "{}" command'.format(apiv, command),
                            fg='red', err=True)
                raise SystemExit(0)

        for flag in flags:
            if flag in version_dict[command]:
                if not version.parse(version_dict[command][flag][0]) <= version.parse(apiv) <= version.parse(version_dict[command][flag][1]):
                    click.secho('Warning: API Version {} does not support "{} --{}" flag,'
                                ' ignorning'.format(apiv, command, flag),
                                fg='yellow', err=True)
