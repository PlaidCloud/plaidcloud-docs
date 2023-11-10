---
title: Installation
slug: install
weight: 2.0
description: Create a configuration file, Install and run the PlaidLink (Agent)
date: 2022-01-25T07:40:17
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
---


## Download the agent

Check the releases on [PlaidCloud.com](https://plaidcloud.com/) for **PlaidLink**

## Extract the agent

Extract the downloaded zip file to an install location of your choice. Generally, this location will be:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Create a configuration file

{{< note >}}
If you are upgrading from a past version of the agent, the configuration file is still valid, and this step can be skipped
{{< /note >}}

Copy the `config-dist.yaml` file in the agent's directory to `%ProgramData\plaidcloud\`, and rename this copy `config.yaml`

*(Edit this configuration with the values retrieved from PlaidCloud)*

## Install the agent's service

Run the `install_windows_service.bat` file in the agent's install directory OR

From an administrator command prompt, navigate to the agent's install directory and run:

```bash
.\PlaidLink.exe install
```

## Running the agent

{{< note >}}
To install a Windows service, one must have administrative privileges
{{< /note >}}

Type **`Services`** into Windows' search bar and open the service manager. In the list of services, find **`PlaidCloud Agent`**.

Right-click the service and select **"Start"** to start the agent.

## Freezing updates

If at any point you want to disable the agent's auto-update feature, open the agent's **'yaml'** configuration file, 
and at the root level of the file, add a line that reads `freeze_updates: true`, and restart the agent's service. 

{{< caution >}}
Disabiling auto-updates is not recommended long-term
{{< /caution >}}
