import click


@click.command()
@click.pass_obj
def user(zahar):
    """This command retrieves users."""

    try:
        user = zahar.zapi.user.get()
        click.echo(user)
    except:
        click.echo('error')

