---
title: Notify Via SMS
description: Send a text message from a workflow step to workspace members who opted in to text alerts, with delivery confirmation, email fallback, repeat collapsing and quiet hours.
sidebar:
  order: 7
---

## Description

Text workspace members when a workflow needs their attention. A text goes only to a member who opted in themselves, from **Text alerts** in the user menu, with a US mobile number they confirmed. You choose members or a distribution list; you never type a phone number into the step. To opt in, see [Text Alerts](/guides/workflows/text-alerts/).

Texts are US numbers only. Don't put health or financial personal data in a text.

Texts come from one PlaidCloud alert number and read `PlaidCloud [your workspace name]: ` followed by your message. See the [SMS Terms](https://plaidcloud.com/sms-terms/) and [SMS Privacy Policy](https://plaidcloud.com/sms-privacy/).

## Recipients

Choose **Members** or **Distribution list**.

- **Members** lists your workspace members. Each shows **Opted in**, **Not opted in**, or **Opted out - Text START to the alert number**.
- **Distribution list** texts every member of the list who has opted in.

A member who hasn't opted in gets no text. They are a problem for the step (see **If a text can't be delivered**), and by default they receive the message by email instead.

## Message

Write the **Message**. Project Variables and Workflow Variables work, and **Insert variable** adds any of these:

| Variable | Value |
|---|---|
| `{workflow_name}` | The name of the running workflow |
| `{project_name}` | The name of the project |
| `{run_url}` | A link to the run in PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | The existing variables |

The counter under the message shows about how many characters and segments the text takes, including the `PlaidCloud [workspace]:` prefix and the run link. A text is cut short past 3 segments. Links from public link shorteners are rejected.

## Delivery

| Setting | What it does |
|---|---|
| **If a text can't be delivered** | **Fail the step** (default) or **Warn and continue**. A text that isn't delivered is never silent: it is always reported on the step. |
| **Email recipients whose text can't be delivered** | On by default. A member whose text fails, who hasn't opted in, or who opted out receives the message by email. |
| **Collapse repeats for (minutes)** | Default 60. A repeat of the same message to the same member within this time isn't sent, and the next text that goes out ends with `(+N similar since HH:MM)`. |
| **Hold texts during quiet hours** | Choose **From** and **to** times and a timezone. A text that would go out inside the window is held until it ends. |

Each member receives at most 20 texts per day, a workspace sends at most 500 texts and fallback emails per day, and one step texts at most 50 members at a time.

## Send Test to Me

**Send test to me** sends a test text to your own number and shows the outcome beside the button. If you haven't opted in, the **Text alerts** window opens so you can.

## What Recipients See

Every text is from the alert number. Replying **STOP** stops all texts from PlaidCloud to that number, and **HELP** returns contact information. After STOP, a member text **START** to the alert number to resume, then turn text alerts back on in **Text alerts**. The step form shows **Opted out - Text START to the alert number** beside that member until they do.

Workspace admins can see each member's text alert status, with the number masked, on the **Member Info** tab of the member window. Members opt in and out themselves; an admin can't do it for them.

## Steps That Typed a Number

An earlier version of this step took a mobile provider and a typed phone number. Those steps now fail with *This step texts a typed number. Choose members who've opted in to text alerts.* Open the step, choose members or a distribution list, and save.

## Examples

No examples yet...
