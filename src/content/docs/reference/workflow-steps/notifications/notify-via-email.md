---
title: Notify Via Email
description: Send email notifications from a PlaidCloud workflow step with customizable subject, body, recipients, and attachment options.
sidebar:
  order: 3
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



### Template Mode (Jinja)


Set **Template Body** to a Jinja template to render a rich HTML email over one or more **Frames** (each naming a single workflow table), instead of the plain `{token}` **Message** body. Leaving Template Body empty keeps the plain-text path above unchanged.

Template mode is a separate, sandboxed rendering engine from the plain-text path — the legacy `{project}` / `{model}` / `{date}` tokens don't resolve inside it. See [Send Templated HTML Email Notifications](/guides/workflows/notify-email-templates/) for the available template variables, the `render_table` helper, the HTML tags and attributes that survive the email sanitizer, and how migrating an existing `{var}` body works.



## Examples


In this example, all of the system variables are used. Additionally, there is a small bit of HTML used to format the first line of the body. Executing this transform will send the following email:


* TO: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* FROM: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (remember that all messages come from this address)
* Subject: DEMO – Workflow Analyze Demo Running
