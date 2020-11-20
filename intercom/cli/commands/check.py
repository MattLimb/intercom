import click
from intercom import IntercomConfig, all_outputs

@click.command("check", help="Check for new tags in the given repos.")
@click.option("-c", "--config", "config", type=str, default="./intercom.yaml", help="Specify a configuration file to use.")
@click.option("-o", "--output", "output", type=str, default="stdout", help="Specify the output to use.")
@click.option("-u", "--no-update", "no_update", is_flag=True, help="Disable the automatic update of the specified config file.")
def check(config, output, no_update):
    config = IntercomConfig(config_location=config)

    for repo in config:
        latest = repo.get_latest()
        if latest != repo.tag:
            all_outputs[output](config, repo).new(repo.tag, latest)
            
            if no_update == False:
                config.update(f"software.{str(repo)}.tag", latest, save=True)
        else:
            all_outputs[output](config, repo).same(repo.tag, latest) 