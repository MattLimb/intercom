import click
from intercom import IntercomConfig, all_outputs, all_overrides

__author__ = "Matt Limb <matt.limb17@gmail.com>"

@click.command("check", help="Check for new tags in the given repos.")
@click.option("-c", "--config", "config", type=str, default="./intercom.yaml", help="Specify a configuration file to use.")
@click.option("-u", "--no-update", "no_update", is_flag=True, help="Disable the automatic update of the specified config file.")
@click.option("-o", "--output", "output", type=str, default=None, help="Override the configuration file and output to stdout.")
def check(config, no_update, output):
    config = IntercomConfig(config_location=config)

    for repo in config:
        latest = repo.get_latest()
        if output == None:
            for _output in config.get("outputs", {}).keys():
                out = config.get(f"outputs.{_output}", {})
                if str(repo) in out["software"]:
                    if latest != repo.tag:
                        all_outputs[out["type"]](config, repo).new(repo.tag, latest, _output)
                        if no_update == False:
                            config.update(f"software.{str(repo)}.tag", latest, save=True)
                    else:
                        all_outputs[out["type"]](config, repo).same(repo.tag, latest, _output) 
        elif output in all_overrides.keys():
            all_overrides[output](config, repo).override(str(repo), repo.tag, latest, f"override-{output}")
        else:
            click.echo(f"Unknown override output {output}")
            quit()
