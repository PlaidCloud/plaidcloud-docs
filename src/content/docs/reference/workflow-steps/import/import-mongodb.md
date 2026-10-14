---
title: Import MongoDB
description: Read a MongoDB collection, or the result of an aggregation pipeline, into a PlaidCloud table as a workflow step.
sidebar:
  order: 17
---

## Description

Reads the documents of a MongoDB collection into a project table, one row per document. Use a filter to read only the documents you need, or an aggregation pipeline to reshape them in MongoDB before they land. The step reaches MongoDB through a [MongoDB connection](/reference/connectors/databases/mongodb/).

## Source and Target

| Setting | Required | What it does |
| --- | --- | --- |
| MongoDB Connection | Yes | The connection to read through. |
| Database | No | The database to read. Leave it blank to use the connection's **Default Database**. |
| Collection | Yes | The collection to read. |
| Target Table | Yes | The table the documents land in. It must be a table, not a view. |

## Query

| Setting | What it does |
| --- | --- |
| Filter (JSON) | A MongoDB query filter as a JSON object, such as `{"status": "open"}`. Only matching documents are read. |
| Aggregation Pipeline (JSON) | An aggregation pipeline as a JSON array, such as `[{"$match": {"status": "open"}}]`. When set, the collection is aggregated instead of filtered. A pipeline with a `$out` or `$merge` stage is refused, because it would write to MongoDB. |
| Row Limit (0 = All) | The most documents to read. `0` reads every one. |
| Time Limit (Seconds) | How long MongoDB may spend on the read before it stops it. |

The filter and the pipeline take workflow variables written as `{name}`, such as `{"region": "{region}"}`. Each variable's value is inserted as a single JSON string or number, so a variable can't add keys or operators to the query. A variable that isn't defined stops the step with an error that names it.

## Column Mapping

Map each document field to a column of the target table on the mapping tab. A column reads the document field of the same name.

## Related

- [Export MongoDB](/reference/workflow-steps/export/export-mongodb/)
- [MongoDB connection](/reference/connectors/databases/mongodb/)
