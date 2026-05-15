---
title: PlaidLink
description: Install and configure PlaidLink agents for secure access to systems behind firewalls, enabling remote queries and file transfers.
sidebar:
  label: PlaidLink
---

PlaidLink provides indirect access to client systems and processes that are protected by firewalls or behind other restrictions that make direct connections from within PlaidCloud difficult. By using a PlaidCloud Agent installed within the isolated area, PlaidCloud can request the agent perform actions like running queries, downloading or uploading files, checking sensor conditions, interacting with SAP, and much more.

Since the agent initiates contact with PlaidCloud and communicates over standard HTTPS network protocols, it can normally operate with minimal setup. In addition, the agent can run as an unprivileged user to control access rights within a restricted environment.

## Topics

- [Install](/reference/cli/plaidlink/install/) — getting PlaidLink running on Windows, Linux, macOS, or in a container
- [Configure](/reference/cli/plaidlink/configure/) — connection settings, credentials, and runtime options
- [Agents](/reference/cli/plaidlink/agents/) — managing multiple agents and their capabilities
- [Upgrade](/reference/cli/plaidlink/upgrade/) — moving to a newer PlaidLink build
