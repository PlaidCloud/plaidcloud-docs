---
title: Export MongoDB
description: Write a PlaidCloud table into a MongoDB collection as inserted, replaced, updated, or upserted documents.
sidebar:
  order: 9
---

## Description

Writes each row of a project table to a MongoDB collection as a document. The collection is created when it doesn't exist. The step reaches MongoDB through a [MongoDB connection](/reference/connectors/databases/mongodb/).

## Source and Target

| Setting | Required | What it does |
| --- | --- | --- |
| Source Table | Yes | The table to write. |
| MongoDB Connection | Yes | The connection to write through. |
| Database | No | The database to write. Leave it blank to use the connection's **Default Database**. |
| Collection | Yes | The collection to write. |

## Write Options

| Setting | What it does |
| --- | --- |
| Write Mode | **Insert a Document per Row** (the default), **Replace the Matching Document**, **Update Fields of the Matching Document**, **Replace the Matching Document, or Insert**, or **Update Fields of the Matching Document, or Insert**. |
| Match Columns | The comma-separated columns that identify a document. Required for every mode but insert. |
| Delete every document in the collection before writing | Empties the collection first, so it holds only this run's rows. |
| Stop at the first failed write | Stops at the first document MongoDB refuses. Clear it to carry on with the rest. |
| Wait for the write to reach the journal | Waits until MongoDB has written each batch to its journal. |
| Write Concern | Blank for the connection's, a number of servers, or `majority`. |
| Documents per Request | How many documents are sent in each request. |

Insert adds the documents again each time the step runs. The modes that replace or update leave the collection the same however many times the step runs, so use one of them when a workflow may run twice over the same rows.

## Related

- [Import MongoDB](/reference/workflow-steps/import/import-mongodb/)
- [MongoDB connection](/reference/connectors/databases/mongodb/)
