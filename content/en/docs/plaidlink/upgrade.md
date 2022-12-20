---
title: Upgrade
slug: upgrade
description: Perform a manual upgrade of the PlaidLink Agent installation
date: 2022-12-20
tags:
- plaidcloud
- plaidlink
categories:
- PlaidCloud
- PlaidLink
---

A manual upgrade of PlaidLink may be necessary if the agent does not have sufficient privileges to update itself when new versions are released or a manual upgrade process is desired.

## Download the agent

Check the releases on [PlaidCloud.com](https://plaidcloud.com/) for **PlaidLink**

## Stop the Current Agent

Type **`Services`** into Windows' search bar and open the service manager. In the list of services, find **`PlaidCloud Agent`**.

Right click on the **`PlaidCloud Agent`** service and select *Stop*.  Once the service successfully stops, continue on.

## Extract the agent

Navigate to the current location of the installed agent.

```bash
C:\Users\<Username here>\src\
```

Rename the current installation folder so that it will no longer be referenced.  For example `Plaidlink_Old_12122022`

Extract the downloaded zip file to an install it in this location. Generally, this location will be:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Start the agent

Return to the *Services* window.  Right click on the **`PlaidCloud Agent`** service and select *Start*.

Type **`Services`** into Windows' search bar and open the service manager. In the list of services, find **`PlaidCloud Agent`**.

Right-click the service and select **`Start`** to start the agent.  Once the agent shows in the **`Running`** state, the agent is now operational again on the new version.
