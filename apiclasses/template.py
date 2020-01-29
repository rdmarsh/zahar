import click

@click.command()
def template():
    """This command retrieves templates."""
    click.echo('template function')

