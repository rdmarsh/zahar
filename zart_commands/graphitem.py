import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve graphitems')
@options.add_options(options.gitemids)
@options.add_options(options.graphids)
@options.add_options(options.itemids)
@options.add_options(options.type)
@options.add_options(options.expandData)
@options.add_options(options.selectGraphs)
@click.option('--sortfield', type=click.Choice(['gitemid']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.sortorder)
@click.pass_obj
def graphitem(zart, sortfield, **kwargs):
    """This command retrieves graphitems."""
    zart.command = 'graphitem'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
