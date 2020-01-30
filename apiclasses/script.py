import click


@click.command()
def script():
    """This command retrieves scripts."""
    click.echo('script function')
