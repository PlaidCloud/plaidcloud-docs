---
title: Notify via Slack
slug: notify-via-slack
weight: 6.0
description: Send Slack notifications
date: 2022-01-25T07:39:49
---


Adding Slack notifications from a workflow is a two part process. The two parts are:


1. Create a Slack Webhook external connection
2. Add Slack notification steps to your workflows

## Add Slack Notification Step to Workflow


Adding Slack notification steps to the workflow is the same as adding other steps to a workflow. Upon adding the step, open the step configuration, complete the form, and save it. You can now test your Slack notification.



## Formatting the Slack Message


Slack has many formatting options including adding images and mentioning users. Please reference the [Slack Text Formatting](https://api.slack.com/reference/surfaces/formatting) documentation for details.



## Create Slack Webhook External Connection


This is a one-time setup to allow PlaidCloud to send Slack notifications on your behalf. Slack allows creation of a Webhook App (a generic way to send a notification over the internet). After creating the Webhook App in Slack, add the supplied credentials to PlaidCloud to allow its use.



### Slack Webhook App Creation


These steps will need to be performed by a Slack administrator. Follow these steps to create a Slack Webhook App:


1. From Slack, open the workspace control menu and select `Settings & administration > Manage Apps`
2. Select `Custom Integrations` from the Apps category list
3. Select `Incoming Webhooks` from the list of apps
4. Select the `Add to Slack` button
5. On the next screen, select the Slack Channel you wish to post the messages and continue. This is the default channel that will be used but it can be overridden in each notification including sending DMs to specific individuals.
6. Copy the webhook URL displayed. This will be used later so keep it in a safe place. It will look something like this: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. You can customize the appearance, name, and emoji before saving. These customizations are only the defaults and these can be overridden on each notification step within a PlaidCloud workflow.

### PlaidCloud External Connection Setup


These steps will need to be performed by a PlaidCloud workspace administrator with permissions to create External Data Connections. Follow these steps to create the connection:


1. Navigate to `Analyze > Tools > External Data Connections`
2. Under the `+ New Connection` selection, pick Slack Webhook
3. Complete the name, description, and paste in the webhook url provided in step 6 above. The name provided here will be shown as the selection in the workflow step so it should be descriptive if possible.
4. Select the `+ Create` button


## Examples

No examples yet...
