import click

@click.command()
def host():
    """This command retrieves hosts."""
    click.echo('host function')

