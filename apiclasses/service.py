import click

@click.command()
def service():
    """This command retrieves services."""
    click.echo('service function')

