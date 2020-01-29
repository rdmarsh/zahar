import click

@click.command()
def event():
    """This command retrieves events."""
    click.echo('event function')

