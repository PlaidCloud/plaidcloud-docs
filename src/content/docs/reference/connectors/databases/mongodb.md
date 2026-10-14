---
title: MongoDB
description: Set up a MongoDB connection in PlaidCloud to read collections into tables and write tables back as documents.
sidebar:
  order: 1
---

**MongoDB** is a document database. Use this connection with [Import MongoDB](/reference/workflow-steps/import/import-mongodb/) to read a collection, or the result of an aggregation pipeline, into a table, and with [Export MongoDB](/reference/workflow-steps/export/export-mongodb/) to write a table back as documents. To create one, choose **MongoDB** as the connection type.

## Upstream Documentation
[The MongoDB documentation](https://www.mongodb.com/docs/).

## Configuration

### MongoDB Connection

| Field | Required | Description |
|---|---|---|
| Host | Yes | The server's host name. |
| Use an SRV address (mongodb+srv://, no port) | No | Connect through a DNS seed list, as MongoDB Atlas does. The port is not used. |
| Port | No | The server's port. Defaults to `27017`. |
| Default Database | No | The database a step uses when it names none. |

### Auth Credentials

| Field | Description |
|---|---|
| User | The user to connect as. |
| Password | The user's password (write-only). |

### Options

| Field | Description |
|---|---|
| Connection Options | MongoDB URI options joined by `&`, such as `authSource=admin&tls=true`. Only the options PlaidCloud allows are accepted. Leave it blank on edit to keep the saved options. |

### TLS

| Field | Description |
|---|---|
| CA Certificate (PEM) | The certificate authority that signed the servers' certificates, when it is not a public one. Leave it blank on edit to keep the saved certificate. |
