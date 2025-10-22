---
title: Paycor REST Connector
slug: paycor-connector
description: Connecting to Paycor from PlaidCloud using REST
weight: 1.0
date: 2025-10-21T07:39:51
---

## API Documentation
The API documentation is for this connector is located [here](https://developers.paycor.com/explore).

## Paycor Setup
The Paycor API Application and Initiation process is a little more involved than other REST providers.  Please be sure to go through the steps outlined on their [Quick Start Page](https://developers.paycor.com/guides#quickStartLabel)

Key values you must capture are:
 - Application OAuth Client ID
 - Application OAuth Client Secret
 - APIm Subscription Key
 - Scope Key of `current` application version

{{< caution >}}
Do not forget to "activate" the application to allow use
{{< /caution >}}

Activate it here, choosing Production or Sandbox depending on your need:

| Environment | Activation Form URL |
|-------------|---------------------|
| Sandbox	  | https://hcm-demo.paycor.com/AppActivation/ClientActivation |
| Production  | https://hcm.paycor.com/AppActivation/ClientActivation |

{{< warning >}}
If you have multiple organizations in Paycor, you will need separate logins for each organization.  DO NOT merge them.  The Developer Portal needs a dedicated unique login for each organization in order to create an organization specific Application for REST access.
{{< /warning >}}

## Security Requirements
Documentation under development

## Obtain Credentials
Documentation under development

## Create REST Connector
Documentation under development
