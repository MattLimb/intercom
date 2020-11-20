# intercom

Track open source software releases. 

intercom is built using Python 3.6 and above.

## Features

- Projects hosted in GitHub
- Projects hosted in GitLab
- YAML Configurtion
- Automatic update of latest tag
- Ability to output to Standard Output
- Ability to ouptput to JSON

## Planned Features

- BitBucket project suppport
- Enterprise Hosted GitHub
- Enterprise Hosted GitLab
- Ability to output a Webhook
- Ability to output to MS Teams

## Configuration

intercom uses YAML as its configuration format.

The base file looks like this:

```yaml
software:
  ...
```

There is only one key for now, called `software`. This is where all our configuration will go.


__NOTE__: There are no limits to the amount of repositories that can be monitored. The program execution length will take longer as more are added.

__NOTE__: For this program to work, each repository configured, must use the "Releases" function of GitHub or GitLab.

### Adding a GitHub Project

GitHub projects are defined like this:

```yaml
<name>:
  service: github
  tag: <latest_tag>
  url: <github_web_url>
```

| Key                | Description                                                                             |
| ------------------ | --------------------------------------------------------------------------------------- |
| `<name>`           | A friendly name of the GitHub repository                                                |
| `<latest_tag>`     | Any tag name. Typically this is the latest one                                          |
| `<github_web_url>` | The GitHub repository url. The link that would take you to GitHub repo in a web browser |

Add this section under the `software` section. For example, a configuration for `PyGithub` would look like this:

```yaml
pygithub:
  service: github
  tag: v1.5.3
  url: https://github.com/PyGithub/PyGithub
```

### Adding a GitLab Project

GitLab projects are defined like this:

```yaml
<name>:
  service: gitlab
  tag: <latest_tag>
  project_id: <project_id>
```

| Key            | Description                                              |
| -------------- | -------------------------------------------------------- |
| `<name>`       | A friendly name of the GitHub repository                 |
| `<latest_tag>` | Any tag name. Typically this is the latest one           |
| `<project_id>` | The project ID listed under the name of a GitLab project |

Add this section under the `software` section. For example, a configuration for `OpenRGB` would look like this:

```yaml
openrgb:
  service: gitlab
  tag: release_0.4
  project_id: 10582521
```


### Example YAML

A full example YAML file would look something like this:

```yaml
software:
  elasticsearch:
    service: github
    tag: v6.8.13
    url: https://github.com/elastic/elasticsearch
  wazuh:
    service: github
    tag: v4.0.0
    url: https://github.com/wazuh/wazuh
  openrgb:
    service: gitlab
    tag: release_0.4
    project_id: 10582521
  gtlab:
    service: gitlab
    tag: v13.6.0-rc46-ee
    project_id: 278964
```

## intercom Usage

### Verify Configuration

```sh
python3 -m intercom verify -c <path_to_config_file>
```

This will check the config file and report any errors found to the Standard Output.

Change `<path_to_config_file>` to the filepath of the YAML config file you added.

### Check Tags

```sh
python3 -m intercom check -c <path_to_config_file>
```

This will check each software configured and check if there are updates to the tag.

The `-c` / `--config` option is required for intercom to work.

#### Optional Options

| Option               | Description                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `-u` / `--no-update` | Do not update the YAML file with the new tags                                                                        |
| `-o` / `--ouput`     | Choose an output method. Currently `stdout` and `json` are supported. `json` output to stdout just in a JSON format. |

## Installation

### Pip Install with Git

This method will require git to be installed, and will install all requirements for you.

For Windows users, replace `python3` with `python`.

```
python3 -m pip install git+https://github.com/MattLimb/intercom.git@intercom
```

### Manual Clone
1. Clone the Repository

```sh
git clone https://github.com/MattLimb/intercom.git
```

2. Change Directory into `intercom`.
   
```sh
cd intercom
```

3. Run `setup.py`

For Windows users, replace `python3` with `python`.

```sh
python3 setup.py
```
