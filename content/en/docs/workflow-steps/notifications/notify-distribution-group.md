---
title: Notify Distribution Group
slug: notify-distribution-group
weight: 1.0
description: Send an email to a PlaidCloud distribution group
date: 2022-01-25T07:40:18
---

## Description


Send an email notification to a PlaidCloud distribution group. Messages are sent from *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. No outbound setup is required.



## Select PlaidCloud Distribution List


Select a single distribution list from the drop down menu. Distribution lists can be created using Tools. For details on creating a distribution list, see here: [PlaidCloud Tools – Distro](/iam/iam/member-management/#managing-distribution-distro-lists).



## Message


Specify **Subject** and **Body** as desired.



Please note that both Project Variables and Workflow Variables are available for use with this transform, in both the subject line and the message body.



Additionally, standard HTML code is permitted in the body to further customize the look of the email messages.


## Examples


In this example, all of the system variables are used. Additionally, there is a small bit of HTML used to format the first line of the body. Executing this transform will send the following email to all members specified in the distribution group:


* FROM: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (remember that all messages come from this address)
* Subject: DEMO Analyze Demo Running


{{< note >}}
Individual recipients of the email message will **not** be able to see the names of other members on the distribution list.
{{< /note >}}


