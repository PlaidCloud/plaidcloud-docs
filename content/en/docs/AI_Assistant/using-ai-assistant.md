---
title: Using the AI Assistant
slug: using-ai-assistant
weight: 1.0
description: Chat with the PlaidCloud AI Assistant — manage conversations, see token usage, and let the assistant pick the right tools for each question.
date: 2026-04-28T00:00:00
---


## Description

The AI Assistant lives in the right-hand panel of the PlaidCloud UI. Open it from the **Tools** menu or from the AI button in the project toolbar.

Each message you send becomes part of a conversation thread. Threads persist across sessions, browsers, and devices, so you can pick up where you left off the next time you log in.


## Start a Conversation

1. Open the **AI Assistant** panel
2. Type your question in the input box
3. Press Enter (or click `Send`)

The assistant streams its response back in the panel, including any tool calls it made along the way.


## Manage Past Conversations

The conversation history list shows every thread on this tenant for your user, most recent first.

**To switch to a past conversation:**

1. Click the conversation in the history list
2. The full transcript is restored in the panel

**To delete a conversation:**

1. Hover the conversation in the history list
2. Click the delete icon
3. Confirm in the dialog

{{< note >}}
Deleting a conversation also removes the related tab if one is open.
{{< /note >}}


## Token Usage

Every AI response shows the token usage for that turn — input tokens, output tokens, and a running total for the conversation. Use this to keep an eye on cost as you work.


## Automatic Tool Selection

The assistant decides on its own which tools and which documents to consult for each question. There are no "use tools" or "use documents" toggles; tool selection happens behind the scenes using a retrieval-and-reranker pipeline that scores the available tools against your prompt.

If the answer doesn't use the tool you expected, rephrase the question or include the table, project, or document name explicitly.


## Expression AI

The Expression Editor in workflow steps includes an `AI` button that asks the assistant to draft or fix an expression in place.

1. Open a workflow step that uses expressions (Project Table, Calculate, Filter, etc.)
2. Click the `AI` button in the expression editor
3. Describe the expression you want
4. Review the suggestion and click `Accept` to insert it

Expression AI passes the current step context as JSON so the assistant has the columns and types available when drafting.
