import click

@click.command()
def screen():
    """This command retrieves screens."""
    click.echo('screen function')

