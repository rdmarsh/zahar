import click

@click.command()
def problem():
    """This command retrieves problems."""
    click.echo('problem function')

