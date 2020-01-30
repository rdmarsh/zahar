import click
import pandas as pd


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
