import click

@click.group()
def cli():
    pass

from .commands import verify

cli.add_command(verify)