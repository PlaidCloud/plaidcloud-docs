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



### Cc, Bcc, and Reply-To

**Cc** (`cc_address`), **Bcc** (`bcc_address`) and **Reply-To** (`reply_to`) take addresses formatted like the recipients, and accept Project and Workflow Variables. Cc and Bcc recipients get the same message, and replies go to the Reply-To address. They apply to plain and Jinja template bodies. Set them with an AI assistant or the REST API.

### One Email for Each Row

Set `request_source` to `table` and name a `driver_table` to send one email for each row of a table instead of a single email. `row_limit` caps the rows used and defaults to 10,000. The driver must be a table, not a view.

Use `{{row.column}}` in the addresses, subject, message and attachment path to fill in each row's value. A column the driver table doesn't have fails the step. A row with no To address sends nothing for that row and the step finishes with a warning that names it.

An attachment path filled from a row (`{{row.column}}`) must be a single existing file, never a folder, so a row whose path came out wrong can't send someone else's files. A row whose value for that path is empty, whose path climbs out of its folder with `..`, or whose file is missing is sent without the attachment, with a warning that names the row. Per-row sending needs a plain body and is not available with a Jinja template body.

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
