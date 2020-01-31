import click
from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve service slas')
@common.add_options(common.serviceids)
@common.add_options(common.intervals)
@click.pass_obj
def servicesla(zart, **kwargs):
    """This command retrieves service slas."""

    # ben magic, throw away False and Empty items
    keywords = {k:v for k,v in kwargs.items() if v}

    try:
        obj = zart.zapi.service.getsla(**keywords)
    except:
        # todo: fix bare except above and write a better error messages
        click.secho('Error: todo.',
                    fg='red', err=True)

    # todo: this is probably not working, getsla needs to be in engine.py
