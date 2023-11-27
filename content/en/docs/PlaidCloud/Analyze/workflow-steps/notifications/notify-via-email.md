---
title: Notify Via Email
slug: notify-via-email
weight: 3.0
description: Send email notifications
date: 2022-01-25T07:39:57
---


## Description


Send email notifications. Messages are sent from *[info@tartansolutions.com](mailto:info@tartansolutions.com)* email account. No outbound setup is required.



### Email Addresses


Specify any number of email recipients. Acceptable delimiters include semicolon (;) and comma (,).



### Message


Specify **Subject** and **Body** as desired.



Please note that both Project Variables and Workflow Variables are available for use with this transform, in both the subject line and the message body.



Additionally, standard HTML code is permitted in the body to further customize the look of the email messages.


### Attachments


Attaching files to emails is very simple. Select a file or folder from Document to attach. If a folder is selected, the contents of the folder will be attached as individual files. Variable substitution works with paths for better control of file attachments when sending out personalized emails.



## Examples


In this example, all of the system variables are used. Additionally, there is a small bit of HTML used to format the first line of the body. Executing this transform will send the following email:


* TO: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* FROM: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (remember that all messages come from this address)
* Subject: DEMO – Workflow Analyze Demo Running
