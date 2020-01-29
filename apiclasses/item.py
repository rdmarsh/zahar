import click

@click.command()
def item():
    """This command retrieves items."""
    click.echo('item function')

