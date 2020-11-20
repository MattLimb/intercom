import click
from intercom import IntercomConfig, all_outputs

@click.command("check", help="Check for new tags in the given repos.")
@click.option("-c", "--config", "config", type=str, default="./intercom.yaml", help="Specify a configuration file to use.")
@click.option("-o", "--output", "output", type=str, default="stdout", help="Specify the output to use.")
def check(config, output):
    config = IntercomConfig(config_location=config)

    for repo in config:
        latest = repo.get_latest()
        all_outputs[output](config, repo).run(repo.tag, latest)
        
        