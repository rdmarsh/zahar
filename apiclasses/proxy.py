import click


@click.command()
def proxy():
    """This command retrieves proxys."""
    click.echo('proxy function')
