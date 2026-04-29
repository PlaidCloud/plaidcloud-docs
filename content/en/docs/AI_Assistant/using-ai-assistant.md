---
title: Using the AI Assistant
slug: using-ai-assistant
weight: 1.0
description: Chat with the PlaidCloud AI Assistant — manage conversations, see token usage, and ask the assistant to draft expressions for workflow steps.
date: 2026-04-28T00:00:00
---


## Description

The AI Assistant is a project-scoped chat. Open the project, then click the **AI** tab alongside Home, Workflows, Tables, etc.

The tab is split into two parts: a conversation history list on the left, and a tabbed chat workspace on the right. Each conversation is its own tab, so you can keep several threads open at once.

Conversations persist, so they survive across sessions, browsers, and devices.


## Start a Conversation

1. Open the project's **AI** tab
2. A new chat tab is created automatically; click in the input box at the bottom
3. Type your question and press Enter (or click `Send`)

The assistant streams its response back, including any tool calls it made along the way. Click `+` on the tab bar to start an additional conversation in parallel.


## Manage Past Conversations

The history list on the left of the **AI** tab shows every conversation in this project for your user, most recent first.

**To switch to a past conversation:**

1. Click the conversation in the history list
2. The full transcript opens in a new chat tab (or the existing one if it's already open)

**To delete a conversation:**

1. Right-click the conversation in the history list
2. Select `Delete Thread`

{{< note >}}
Deleting a conversation also closes its chat tab if one is open.
{{< /note >}}


## Token Usage

Every AI response shows the token usage for that turn — input tokens, output tokens, and a running total for the conversation. Use this to keep an eye on cost as you work.


## Automatic Tool Selection

The assistant decides on its own which tools to call and which documents to consult for each question. There are no toggles to choose what's used; tool selection happens behind the scenes by scoring the available tools against your prompt.

If the answer doesn't use the tool you expected, rephrase the question or include the table, project, or document name explicitly.


## Expression AI

The Expression Editor — used by Project Table, Calculate, Filter, and any other step that takes expressions — has the AI Assistant built in as a side panel.

1. Open a workflow step that uses expressions
2. Open the editor for the column you want to fill in
3. The AI panel sits alongside the expression editor; ask it to draft or fix the expression
4. Copy the suggested expression into the editor

The chat already has the column list and types from the current step, so you can ask questions like "concatenate first_name and last_name with a space" without restating the schema.
