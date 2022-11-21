---
title: PlaidLink Agents
slug: plaidlink-agents
description: Create and manage remote access using lightweight agents
date: 2022-01-25T07:39:49
---


## Description


Sometimes it’s necessary and desireable to access data or run processes from a remote system that does not allow external access. This is common in enterprise environments behind firewalls. PlaidCloud allows this ability by using PlaidLink, which enables remote systems access behind a firewall or where direct access from PlaidCloud is not desired.



PlaidLink uses an agent-based system. This means that an agent, the remote user, is installed on a system inside the firewall or other restricted area. The agent can then connect to PlaidCloud by using an outbound initiation process over a secure HTTPS websocket connection. It is as secure as any other encrypted web connection and usually does not require you to open non-standard ports. Before gaining access, the agent must identify itself by sending its agent identifier. From this, if the agent has a successful authentication process, the agent is granted access to the approved operations.



PlaidLink can be installed on Windows, Unix, and Linux systems and can run under low privilege users. On Windows systems, PlaidLink can operate as a Windows Service with full control from the Service panel. On linux or unix systems, it can run as a deamon process.

PlaidLink can also run as a stand-alone Docker container or as a Kubernetes pod.



## Managing Agents


**To manage agents:**


1. Open Analyze
2. Select “Tools”
3. Click “PlaidLink Agents”

This brings you to the **PlaidLink Agents Table** where you can view, modify, and obtain credentials for the list of available agents.



## Creating an Agent


**To create an agent:**


1. Open Analyze
2. Select “Tools”
3. Click “PlaidLink Agents”
4. Click “Add PlaidLink Agent”
5. Complete the required fields
6. Click “Create”
7. Assign the agent to the necessary security groups to access resources needed to perform its job
8. Assign the agent to the necessary Document accounts to access documents needed to perform its job


{{< warning >}}
For Steps 7 and 8 above, the PlaidLink Agent must be assigned to security groups and document accounts necessary
for performing the jobs you expect the Agent to perform.  Otherwise it will be denied access.
{{< /warning >}}

{{< note >}}
Any information not present on the new agent form will be automatically generated.
{{< /note >}}



## Obtaining Agent Credentials


To configure PlaidLink agents on the remote system, you must first obtain the agent’s identifying information in order to maintain security. This information includes both a public and a private key.



**To obtain these keys:**


1. Open Analyze
2. Select “Tools”
3. Click “PlaidLink Agents”
4. Click the edit icon

This will open a form where you can view the public and private key values.


## Regenerating Agent Credentials


It is a good idea to periodically regenerate the public and private keys and update the configuration of remote systems in order to maintain security.



**To regenerate the credentials:**


1. Open Analyze
2. Select “Tools”
3. Click “PlaidLink Agents”
4. Click the regenerate icon

Once the credentials have been regenerated, they can be obtained in the same way a new agent’s credentials are obtained (described above).



## Enabling and Disabling an Agent


**To disable an agent:**


1. Open Analyze
2. Select “Tools”
3. Click “PlaidLink Agents”
4. Uncheck the “Active” checkbox

{{< note >}}
When an agent is not marked as active, remote systems will not be able to connect using those agent credentials
{{< /note >}}



## Running Multiple Agents


PlaidLink is designed to allow operation of multiple agents using a single service installation. Such a streamlined installation system permits one install to handle agents from multiple workspaces and / or agents with different levels of permissions for task execution.

To enable multiple agents, you simply add the agent credentials to the PlaidLink configuration file.

## Running Multiple PlaidLink Services

Similar to running multiple agents within one PlaidLink service, it is also possible to run multiple PlaidLink services.

This is sometimes necessary depending on use of system based security or network access restrictions that prevent communication across network boundaries.

{{< note >}}
It is normally better to run multiple agents under a single service rather multiple services on a single machine.  However, depending on the use case it may be necessary to run multiple distinct services.
{{< /note >}}

## Compute, Memory, and Disk Requirements

The PlaidLink service is extremely lightweight and only needs minimal compute and memory to operate.  When processing significant data volumes it may be necessary to increase compute resources and especially memory.

Normally, the agent will happily run with 5% of CPU and 200MB of memory.  For intense data operations, it is recommended to allocate an entire CPU and at least 4GB of RAM.  For dynamic resource allocation systems like Kubernetes, it is fine if the agent has access to burstable resources rather than reserved resources.

Disk space for the agent is minimal too.  Agent operations utilize disk space as a data buffer when transferring large amounts of data.  Typically, 8GB of space is fine for normal operations.  For intense data operations it is recommended that you scale disk up according to the expected data volumes.  There is no set amount because it depends on several factors including CPU speed, network speed, amount of data, etc...  However, a good place to start is 20GB and adjust from there.


## Networking Requirements

The PlaidLink Agent is designed to operate with minimal configuration required.  It does not require any special VPN or network configuration other than allowing standard HTTPS network traffic.  Agents communicate over the same protocol as normal web browser based traffic.

The agent service always initiates communication with PlaidCloud so there is no need to configure ingress access in firewalls.

{{< note >}}
Sometimes firewall rules block all access, even standard HTTPS traffic.  If the agent reports it is unable to contact PlaidCloud on startup, you will need to work with your networking team to open port 443 for traffic.
{{< /note >}}
