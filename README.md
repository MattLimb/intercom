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
- Ability to output a Webhook

## Planned Features

- BitBucket project suppport
- Enterprise Hosted GitHub
- Enterprise Hosted GitLab
- Ability to output to MS Teams

## Software Configuration

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

## Output Configuration

Outputs are configured using the `outputs` key in the root of the YAML document - similar to the `software` key.

To configure an output, there are only three keys that are required by all outputs:

```yaml
<name_of_output>:
  type: stdout | json | webhook
  software:
    - <software_name>
```

| Key              | Description                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name_of_output` | A friendly name of the output. Is outputted with JSON and webhooks so that you can know where the request came from                                                                                     |
| `type`           | The output that is desired - either stdout, json or webhook                                                                                                                                             |
| `software`       | The friendly names of the OSS you set up in the `software` root key. They are a list, so need to start with a `-` as shown in the example. There is no limit to how many pieces of software per output. |

### stdout Output

This output type, outputs to the Standard Output of the terminal in the following format:

```sh
New Tag for <software_name>: <tag>
```

There are no additional configuration needed for the `stdout` output.

### json Output

This ouput type, outputs to the Standard Output of the terminal in JSON in the following format:

```json
{
  "repo": "<software_name>",
  "oldTag": "<old_tag_name>",
  "newTag": "<new_tag_name>",
  "message": "New release for <software_name> - <new_tag_name>",
  "output": "<output_name>"
}
```

There are no additonal configuration needed for the `json` output.

### webhook Output

This output type will send a post request to a given url. The JSON sent will be in this style:

```json
{
  "repo": "<software_name>",
  "oldTag": "<old_tag_name>",
  "newTag": "<new_tag_name>",
  "message": "New release for <software_name> - <new_tag_name>",
  "output": "<output_name>"
}
```

The `webhook` output does require some additional coonfiguration:

| Key    | Description                                                                 |
| ------ | --------------------------------------------------------------------------- |
| `url`  | The URL to send the POST request to.                                        |
| `auth` | What type of authentication to send with the request: none, basic or bearer |

### `none` Authentication

No authentication will be sent. No other configuration keys are needed.

```yaml
webhook-no-auth:
  type: webhook
  software:
   - wazuh
  url: http://localhost:5000
  auth: none
```

### `basic` Authentication

This will send the `Authorization` header for HTTP Basic Authentication.

This will require two additional keys, `username` and `password`:

```yaml
webhook-basic-auth:
  type: webhook
  software:
   - wazuh
  url: http://localhost:5000
  auth: basic
  username: user
  password: pass
```

### `bearer` Authentication

This will send the `Authorization` header for HTTP Basic Authentication..

This will require 1 additional key, from the base webhook config, `token`. `token` is the bearer token or api key of the service.

```yaml
webhook-basic-auth:
  type: webhook
  software:
   - wazuh
  url: http://localhost:5000
  auth: bearer
  token: SOME_TOKEN
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


All outputs are now specified in the configuration file.

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
