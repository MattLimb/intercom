import click
from intercom import IntercomConfig

@click.command("verify", help="Verify that the configuration file is correct.")
@click.option("-c", "--config", "config", type=str, default="./intercom.yaml", help="Specify a configuration file to use.")
def verify(config):
    config = IntercomConfig(config_location=config)

    for message in config.verify_config():
        click.echo(message)