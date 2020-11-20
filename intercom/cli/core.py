import click

__author__ = "Matt Limb <matt.limb17@gmail.com>"

@click.group()
def cli():
    pass

from .commands import verify
from .commands import check

cli.add_command(verify)
cli.add_command(check)