import logging
import json
import click
import pandas as pd
from packaging import version
from jinja2 import Environment, FileSystemLoader
from pygments import highlight, lexers, formatters
from collections import defaultdict


log = logging.getLogger(__name__)


def engine(zart, **kwargs):
    """This is common engine for all commands."""

    if zart.command == 'apiinfo':
        click.echo(zart.apiv)
        return

    # ben magic, throw away False and Empty flags
    flags = {k: v for k, v in kwargs.items() if v}
    logging.info('passed flags: %s', flags)

    # version checks
    version_check(zart.apiv, zart.command, flags.keys())

    # todo: somehow make better
    for select in [
        'selectFilter',
        'selectConditions',
        'selectMessageTemplates',
        'selectInheritedTags',
        'selectDetails',
        'selectOperations',
        'selectRecoveryOperations',
        'selectHosts',
        'selectMediatypes',
        'selectUsers',
        'selectHost',
        'selectItems',
        'selectDiscoveryRule',
        'selectApplicationDiscovery',
        'selectWidgets',
        'selectUserGroups',
        'selectDRules',
        'selectDServices',
        'selectDHosts',
        'selectDChecks',
        'selectRelatedObject',
        'select_alerts',
        'selectGraphs',
        'selectTagFilters',
        'selectTags',
        'selectLastEvent',
        'selectGroups',
        'selectParentTemplates',
        'output',
        ]:
        try:
            flags[select]
            logging.info(flags[select])

            if 'extend' in flags[select]:
                flags[select] = 'extend'
            if 'count' in flags[select]:
                flags[select] = 'count'
        except:
            pass


    #filters and search need to be dicts
    #https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory
    if 'filter' in flags and flags['filter']:
        filter_dict = defaultdict(list)
        for k, v in flags['filter']:
            filter_dict[k].append(v)
        flags['filter'] = dict(filter_dict.items())
        logging.info(flags['filter'])

    if 'search' in flags and flags['search']:
        search_dict = defaultdict(list)
        for k, v in flags['search']:
            search_dict[k].append(v)
        flags['search'] = dict(search_dict.items())
        logging.info(flags['search'])

    try:
        obj = getattr(zart.zapi, zart.command).get(**flags)
    except:
        click.secho('Error: todo Exception.',
                    fg='red', err=True)

    if zart.export_filename:
        export(zart.export_filename, zart.config_file, zart.command, flags) 

    # print countoutput otherwise send obj to output with format
    if 'countOutput' in flags and flags['countOutput']:
        if str(obj).isdigit():
            click.echo(obj)
        else:
            click.secho('0', fg='yellow')
            click.secho('Warning: no values returned,'
                        ' assuming 0 or this flag is not supported.',
                        fg='yellow', err=True)
    else:
        logging.info('zart.out_fmt: %s', zart.out_fmt)
        outputformat(obj, zart.out_fmt)

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
        elif outputformat == 'pretty-html':
            colorful_html = highlight(df.to_html(index=False), lexers.HtmlLexer(), formatters.TerminalFormatter())
            click.echo(colorful_html)
        elif outputformat == 'json':
            click.echo(df.to_json(orient='records'))
        elif outputformat == 'pretty-json':
            colorful_json = highlight(df.to_json(orient='records'), lexers.JsonLexer(), formatters.TerminalFormatter())
            click.echo(colorful_json)
        elif outputformat == 'latex':
            click.echo(df.to_latex(index=False))
        elif outputformat == 'raw':
            click.echo(obj)
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

def export(export_filename, config_file, command, flags=""):
    '''export python query to file'''
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('save_query.py.j2')
    output = template.render(config_file=config_file, command=command, flags=flags)
    export_filename.write(output)