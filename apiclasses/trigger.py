import click


@click.command()
def trigger():
    """This command retrieves triggers."""
    click.echo('trigger function')
