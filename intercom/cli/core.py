import click

@click.group()
def cli():
    pass

from .commands import verify
from .commands import check

cli.add_command(verify)
cli.add_command(check)