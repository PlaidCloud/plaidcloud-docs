---
title: Getting Started
slug: getting-started
description: Getting started with the PlaidCloud Data Lakehouse Service
weight: 1.0
date: 2022-01-25T07:39:51
---


## About

The PlaidCloud Data Lakehouse Service (DLS) stands on the shoulders of great technology.  The service is based on [Databend](https://github.com/PlaidCloud/databend), a lakehouse suitable for big data analytics and traditional data warehouse operations while supporting vast storage as a data lake.  It's extensive analytical optimizations, array of indexing types, high compression, and native time travel capabilities makes it ideal for wide array of uses.

The PlaidCloud DLS also has the ability to integrate with existing data lakes on Apache Hive, Apache Iceberg, and Delta Lake.  This allows for accessing vast amounts of already stored data using a modern and fast query engine without having to move any data.

The PlaidCloud DLS continues our goal of providing the best open source options for our customers to eliminate lock-in while also providing services as turn-key solutions.

Managing, upgrading, and maintaining a data lakehouse requires special skills and investment.  Both can be hard to find when you need them.  The PlaidCloud service eliminates that need while still providing deep technical access for those that need or want total control.

## Key Benefits

### Always on

The PlaidCloud DLS provides always-on query access.  You don't have to schedule availability or incur additional costs for usage outside the expected time.

This also means there is no first-query delay and no cache to warm up before optimal performance is achieved.


### Read and Write the way you expect

The PlaidCloud DLS operates like a traditional database so you don't have to decide which instances are read-only or have special processes to load data from a write instance.  All instances support full read and write with no special ETL or data loading processes required.

If you are used to using traditional databases, you don't need to learn any new skills or change your applications.  The DLS is a drop-in replacement for ANSI SQL compliant databases.  If you are coming from other databases such as Oracle, MySQL or Microsoft SQL Server then some adjustments to your query logic may be necessary but not to the overall process.

Since SAP HANA and Amazon Redshift use the PostgreSQL dialect, those seeking a portable alternative will find PlaidCloud DLS a straightforward option.


### Economical

With usage based billing, you only pay for what you use.  There are no per-query or extra processing charges.  Triple redundant storage, incredible IOPS, wide data throughput, time travel queries, and out-of-band backups are all standard at a reasonable price.

We eliminate the headache of having to choose different data warehousing tiers based on optimizing storage costs.  We offer the ability to select how long each table's history is kept live for time travel queries and recovery.

Zero (0) days of time travel creates a transient table that will have no time travel or recovery.  This is suitable for intermediate tables or tables that can be reproduced from other data.

You can set tables to have from one (1) to ninety (90) days of time travel.  During the time travel window you can issue queries to view data at different snapshots or 
periods along with recovery a table at a point-in-time to a new table.  This is an incredibly powerful capability that surpasses traditional backups because the historical state of a table can be viewed with a simple query rather than having to recover a backup.


### Highly performant

While network attached storage has been able to achieve significant performance, it still can't come close to local disk.  Using local disks for storage is complicated while operating in cloud environments but our goal was to provide an uncompromising Data Lakehouse Service that can achieve the same or better performance as a hand-built data warehouse cluster.

We also extensively tested optimal compute, networking, and RAM configurations to achieve maximum performance.  As new technology and capabilities become available, our goal is to incorporate features that increase performance.


### Scale out and scale up capable

The ability to both scale up and scale out are essential for a data lakehouse, especially when it is performing analytical processes.

Scaling up means more simultaneous queries can occur at once.  This is useful if you have many users or applications that require many concurrent processes.

Scaling out means more compute power can be applied to each query by breaking the data processing up across many CPUs.  This is useful on large data where summarizations or other analytical processes such as machine learning, AI, or geospatial analysis is required.

The PlaidCloud DLS allows scale expansion either on-demand or based on pre-defined events/metrics.


### Integrated with PlaidCloud Analyze for Low/No Code operations

Analyze, Dashboards, Forms, and JupyterLab are quickly connected to any PlaidCloud DLS.  This provides point-and-click operations to automate data related activities as well as building beautiful visualizations for reporting and insightful analysis.

From an Analyze project, you can select any DLS instance.  This also provides the ability for Analyze projects to switch among DWS instances to facilitate testing and Blue/Green upgrade processes.  It also allows quickly restoring an Analyze Project from a DLS point-in-time backup.


### Clone

Making a clone of an existing lakehouse performs a complete copy of the source lakehouse.  When a clone is made it has nothing shared with the original lakehouse and therefore is a quick way to isolate a complete lakehouse for testing or even a live archive at a specific point in time.

Another important feature is that you can clone a lakehouse to a different data center.  This might be desireable if global usage shifts from one region to another or having a copy of a warehouse in various regions for development/testing improves internal processes.


### Web or Desktop SQL Client Access

A web SQL console is provided within PlaidCloud.  It is a full featured SQL client so it supports most use cases.  However, for more advanced use cases, a desktop client or other service may be desired.  The PlaidCloud DLS uses standard security and access controls enabling remote connections and controlled user permissions.

Access options allow quick and easy start-up as well as ongoing query and analytics access.  A firewall allows control over external access.

[DBeaver](https://dbeaver.io/download/) provides a nice free desktop option that has a Greenplum driver to fully support PlaidCloud DWS instances.  They also provide a commercial version called [DBeaver Pro](https://dbeaver.com/) for those that require/prefer use of licensed software.
