import click

@click.command()
def maintenance():
    """This command retrieves maintenances."""
    click.echo('maintenance function')

