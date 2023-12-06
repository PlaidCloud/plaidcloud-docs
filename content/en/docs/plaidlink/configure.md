---
title: Configure
slug: configure
weight: 3.0
description: Create and maintain PlaidLink (Agent) documentation and account access for optimal database and file system enhancement
date: 2022-01-25T07:40:17
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
---


The PlaidLink Agent works in conjunction with the PlaidCloud service. The PlaidLink Agent provides the connection necessary 
to operate with systems not accessible directly such as databases and file systems. The agent performs a number of essential actions including:

* Reading and writing to databases
* Reading and writing files to network drives and servers
* Checking for sensor conditions
* Interacting with SAP ECC and SAP S/4HANA through Remote Function Calls (RFCs)
* Interacting with SAP Profitability and Cost Management (PCM)
* Sending messages and notifications to remote systems

## Create an Agent on PlaidCloud

PlaidLink Agent management takes place within the Analyze tab of PlaidCloud. The first step is to create a new PlaidLink Agent instance on PlaidCloud.

### To create a new PlaidLink Agent

1. Select the Analyze tab
2. Select the tools menu from the top
3. Click PlaidLink Agents
4. Create a new Agent with an appropriate name for the environment or server that it will be installed on for remote operations

### To view the Agent public and private keys

1. Click on the edit icon to view the form
2. At the bottom of the form you will find the public and private keys that were randomly generated during the Agent creation process

{{< note >}}
Remember these keys, as they will be used in the agent configuration on the remote server.
{{< /note >}}

### To randomly generate new keys

1. Click on the Regenerate icon for the Agent record
2. Once the keys are regenerated, don’t forget to update the agent configuration file with the new keys on the remote server.

{{< note >}}
Retain the public and private keys for configuring the remote agent in the next step.
{{< /note >}}

## Document Account Access

If the agent will need to have access to a Document account for uploading or downloading files, it must be granted permission to access the Document account.

### To grant account access

1. In the Document tab select Manage Accounts
2. Once the table of accounts appears, click on the agent icon for the account which the new Agent should have upload/download rights
3. Drag the new agent into the Assigned Agents column
4. Save the access control form.

{{< note >}}
Agents can only upload and download files if the agent has been granted access to one or more Document accounts.
{{< /note >}}

## Data Connection Access

If the agent will need to have access to a data connection such as a database, it must be granted permission to access the external data connection information.


### To grant connection access


1. In the Analyze tab select the Tools menu
2. Click External Data Connections
3. Once the table of data connections appears, click on the agent icon for the connection, which the new Agent should have usage rights
4. Drag the new agent into the Assigned Agents column and save the access control form.

{{< note >}}
Agent data connection credentials are managed in the External Data Connections.
{{< /note >}}

### Next Step: Installing PlaidLink (Agent) on a Remote System

Follow these [Installation Instructions](/plaidlink/install) to install PlaidLink on the remote system.
