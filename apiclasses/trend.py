import click


@click.command()
def trend():
    """This command retrieves trends."""
    click.echo('trend function')
