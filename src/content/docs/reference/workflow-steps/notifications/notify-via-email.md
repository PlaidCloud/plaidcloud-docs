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



### Body (Jinja Template)


The step's body is authored as a **Jinja template** rendered over one or more **frames**, producing a rich HTML email. Each frame is a named single-table selection — a Frame Name, one workflow table, and optional column selection, a where filter, and aggregation (no joins). The editor opens directly into this template — the frame list, the template body, a live preview, and a **Send Test to Me** button — with no plain-text-versus-template toggle. A **Prettify** button and an insert palette (`render_table(...)` for a frame, `{{ cloud }}`, a for-loop, and the currency/thousands/percent/date filters) help shape the template.

Reference each frame in the template as `frames['<Frame Name>'].rows` and `frames['<Frame Name>'].columns`; a single-frame template can use the top-level `rows` / `columns`, which are bound to the first frame. The template is a separate, sandboxed rendering engine — only `cloud` resolves as a workspace value, and the legacy `{project}` / `{model}` / `{date}` tokens don't resolve inside it. Steps created before Jinja authoring open with their old body auto-converted; a body that can't be converted safely stays in a plain-text fallback and keeps sending with the legacy `{token}` substitution. See [Send Templated HTML Email Notifications](/guides/workflows/notify-email-templates/) for the available template variables, the `render_table` helper, the HTML tags and attributes that survive the email sanitizer, and how existing bodies migrate.



## Examples


In this example, all of the system variables are used. Additionally, there is a small bit of HTML used to format the first line of the body. Executing this transform will send the following email:


* TO: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* FROM: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (remember that all messages come from this address)
* Subject: DEMO – Workflow Analyze Demo Running
