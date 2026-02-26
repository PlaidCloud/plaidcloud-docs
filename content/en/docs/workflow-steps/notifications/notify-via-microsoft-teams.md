---
title: Notify via Microsoft Teams
slug: notify-via-microsoft-teams
weight: 5.0
description: Send notifications to Microsoft Teams channels
date: 2022-01-25T07:40:21
---


Adding Microsoft Teams notifications from a workflow is a two part process. The two parts are:


1. Create a Microsoft Teams external connection
2. Add Microsoft Teams notification steps to your workflows

## Add Microsoft Teams Notification Step to Workflow


Adding Microsoft Teams notification steps to the workflow is the same as adding other steps to a workflow. Upon adding the step, open the step configuration, complete the form, and save it. You can now test your Microsoft Teams notification.



## Formatting the Microsoft Teams Message


Teams has many formatting options including adding images and mentioning users. Please reference the [Teams Message Text Formatting](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) documentation for details.



## Create Microsoft Teams External Connection


This is a one-time setup to allow PlaidCloud to send Microsoft Teams notifications on your behalf. Microsoft Teams allows creation of a Webhook App (a generic way to send a notification over the internet). After creating the Webhook App in Microsoft Teams, add the supplied credentials to PlaidCloud to allow its use.



### Microsoft Teams Webhook App Creation


These steps will need to be performed by a Microsoft Teams administrator. Follow the steps outlined here for [Creating Incoming Webhook (Microsoft Teams Documentation)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### PlaidCloud External Connection Setup


These steps will need to be performed by a PlaidCloud workspace administrator with permissions to create External Data Connections. Follow these steps to create the connection:


1. Navigate to `Analyze > Tools > External Data Connections`
2. Under the `+ New Connection` selection, pick Microsoft Teams Webhook
3. Complete the name, description, and paste in the webhook url generated during the webhook creation above. The name provided here will be shown as the selection in the workflow step so it should be descriptive if possible.
4. Select the `+ Create` button


## Examples

No examples yet...
