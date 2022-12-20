---
title: Getting Started
slug: getting-started
description: Getting started with the PlaidCloud Data Warehouse Service
date: 2022-01-25T07:39:51
---


## About

The PlaidCloud Data Warehouse Service (DWS) stands on the shoulders of great technology.  The service is based on [Greenplum](https://greenplum.org/), a warehouse suitable for big data analytics and traditional data warehouse operations.  It's extensive analytical optimizations, array of indexing types, highly-flexible compression, and availability of both row-based and columnar storage models makes it ideal for wide array of uses.

Managing, upgrading, and maintaining a data warehouse requires special skills and investment.  Both can be hard to find when you need them.  The PlaidCloud service eliminates that need while still providing deep technical access for those that need or want total control.  Since [Greenplum](https://greenplum.org/) is based on [PostgreSQL](https://www.postgresql.org/), it is nearly 100% compatible with current [PostgreSQL](https://www.postgresql.org/) operations.

## Key Benefits

### Always on

The PlaidCloud DWS provides always-on query access.  You don't have to schedule availability and additional costs for usage outside the expected time.

### Economical

With usage based billing, you only pay for what you use.  There are no per-query or extra processing charges.  High performance storage with triple redundancy, incredible IOPS, wide data throughput, and out-of-band backups are all standard at a reasonable price.

We eliminate the headache of having to choose different data warehousing tiers based on optimizing storage costs.

When query performance is less critical, data can be stored in `Cost Optimized` table types.  This allows use of cloud storage to reduce the cost of storage for data that does not have the same performance requirements as actively queried data.


### Large number of connectors available

Since PlaidCloud DWS is based on [PostgreSQL](https://www.postgresql.org/) technology, virtually all [PostgreSQL](https://www.postgresql.org/) connectors and clients will work out-of-the-box.  With a vibrant [PostgreSQL](https://www.postgresql.org/) community, new capabilities, adapters, and connectors are released frequently.


### Highly performant

While network attached storage has been able to achieve significant performance, it still can't come close to local disk.  Using local disks for storage is complicated while operating in cloud environments but our goal was to provide an uncompromising data warehouse service that can achieve the same or better performance as a hand-built data warehouse cluster.

We also extensively tested optimal compute, networking, and RAM configurations to achieve maximum performance.  As new technology and capabilities become available, our goal is to incorporate features that increase performance.

### Real-time backups without impacting performance

One of the more complex processes with data warehouse clusters is backups.  While seemingly simple, achieving a consistent snapshot of data across many nodes while not interfering in the execution multiple queries is actually quite complex.  Doing this without impacting performance of the database is even harder.

Thankfully, you don't have to worry about all that complexity.  You can set the frequency of backups you desire and it is all handled automatically for you.  While all data is triple redundant, backups are necessary in the event a destructive user action takes place such as accidentally deleting data or dropping a table.  Having a backup allows for recovery of that prior state.


### Well understood and mature

While much of data warehousing activity is fairly straightforward, there still remains a large body of work that pushes the bounds of a database.  When operating at maximum capacity, many facets come into play including the maturity and optimization of all the underlying processes.  Since PlaidCloud DWS is built on very mature technology in use for decades, substantial performance and stability optimizations are in place.

With a well understood and mature technical foundation, there is a far less likelihood of strange failure modes and when unusual events do occur an answer is likely a Google search away.

Tuning queries is sometimes necessary for highly complex queries.  There are substantial resources available that help explain, analyze, and optimize queries in [PostgreSQL](https://www.postgresql.org/) and Greenplum systems.  We all wish that the days of hand tuning queries were no longer necessary. The questions we ask of our data and required processing to determine a result can often have orders of magnitude time improvements by adjusting aspects of the query with even the most intelligent query planner will struggle.

When trying to squeeze out the best performance you want to rely on known patterns and examples.

### Scale out and scale up capable

The ability to both scale up and scale out are essential for a data warehouse, especially when it is performing analytical processes.

Scaling up means more simultaneous queries can occur at once.  This is useful if you have many users or applications that require many concurrent processes.

Scaling out means more compute power can be applied to each query by breaking the data processing across many CPUs.  This is useful on large data where summarizations or other analytical processes such as machine learning ([MADLib](https://madlib.apache.org/)) or geospatial ([PostGIS](https://postgis.net/)) analysis is required.

The PlaidCloud DWS allows scale expansion either on-demand or based on pre-defined events/metrics.

### Integrated with PlaidCloud Analyze for Low/No Code operations

Analyze and Dashboards are quickly connected to any PlaidCloud DWS.  This provides point-and-click operations to automate any data related activities as well as building beautiful visualizations for reporting and insightful analysis.

From an Analyze project, you can select any DWS instance.  This also provides the ability for Analyze projects to switch among data warehouse instances to facilitate testing and Blue/Green upgrade processes.  It also allows quickly restoring an Analyze Project from a data warehouse point-in-time backup.

### Clone

Making a clone of an existing warehouse performs a complete copy of the source warehouse.  When a clone is made it has nothing shared with the original warehouse and therefore is a quick way to isolate a complete warehouse for testing or even a live archive at a specific point in time.

Another important feature is that you can clone a warehouse to a different data center.  This might be desireable if global usage shifts from one region to another or having a copy of a warehouse in various regions for development/testing improves internal processes.

### Restore

A new warehouse instance is easily restored from an existing backup.  The backup frequency is adjustable for each warehouse instance.  Those backups allow for a point-in-time restoration.

### Web or Desktop SQL Client Access

A web SQL console is provided within PlaidCloud.  It is a full featured SQL client so it supports most use cases.  However, for more advanced use cases, a desktop client or other service may be desired.  The PlaidCloud DWS uses standard security and access controls enabling remote connections and controlled user permissions.

Access options allow quick and easy start-up as well as ongoing query and analytics access.  A firewall allows control over external access.
