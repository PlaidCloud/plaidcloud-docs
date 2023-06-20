---
title: Pricing
description: PlaidCloud Data Warehouse Service Pricing
weight: 2
date: 2022-01-25T07:39:51
---


## Usage Based

The cost of a PlaidCloud Data Warehouse instance is determined by a limited number of factors that you control.  All costs incurred are usage based.

The factors that impact cost are:
 - Concurrency Factor - The size of each compute node in your warehouse instance
 - Parallelism Factor - The number of nodes in your warehouse instance
 - Allocated Storage - The number of Gigabytes of storage consumed by your warehouse instance
 - Network Egress - The number of Gigabytes of network egress. Excludes traffic to PlaidCloud applications within the same region.  Ingress is always free.
 - Backup Retention Period - How many days, weeks, or months to retain backups beyond 30 days

Storage, backups, and network egress are calculated in gigabytes (GB), where 1 GB is 2^30 bytes. This unit of measurement is also known as a [gibibyte (GiB)](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units).

All prices are in USD.  If you are paying in another currency please convert to your currency using the appropriate rate.

Billing is on an hourly basis.  The monthly prices shown are illustrative based on a 730 hour month.


## Controlling Factors

### Concurrency Factor

| Compute Type     | Hourly Cost (streams/hr) |  Monthly Cost (streams/month) |
|------------------|--------------------------|-------------------------------|
| Standard         |               $0.0739726 |                           $54 |

Concurrency determines how many simultaneous queries are handled by the DWS instance.  This is expressed as a number of process streams.  There is not a 1:1 relationship between streams and query capacity since a single stream can handle multiple simultaneous queries.  However, as the number of concurrent requests increase, the query duration may exceed the desired response time and an increase in the concurrency factor will help.

From a conceptual standpoint you can view processing streams as vCPUs used to process queries.

The default concurrency factor is 2, which is a good starting point if you are unsure of your needs.  It can be adjusted from 1 to 14.  If your needs exceed 14, please contact us to increase your concurrency limit.


### Parallelism Factor

There is no additional cost per node.  The compute cost of the DWS instance is the product of concurrency and parallelism plus the master node.

Parallelism determines how many nodes are in the DWS instance.  This is expressed as node count.  The number of nodes determines how much compute power can be applied to any single query.  By increasing the node count, the computational part of the query can be spread out over many process streams.  In addition, the storage throughput is multiplied by the number of nodes, which is very valuable when dealing with large datasets.

For example, if the maximum theoretical write throughput of a single node was 4 TB/sec, a warehouse with 8 nodes would have a theoretical write throughput of 8 x 4 TB/sec = 32 TB/sec.  There are many factors that impact write speed including compression level, indexes, table storage type, network overhead, etc... but in general, nodes apply a multiplying factor to data throughput speed.


### Allocated Storage

Three types of table storage options are available in a PlaidCloud DWS:
 - Hot
 - Warm
 - Cold

| Storage Type     | Hourly Cost (GB/hr) |  Monthly Cost (GB/month)  |
|------------------|---------------------|---------------------------|
| Hot              |          $0.0006849 |                     $0.50 |
| Warm             |          $0.0002055 |                     $0.16 |
| Cold             |          $0.0000685 |                     $0.05 |

These storage options can be applied on a table-by-table basis so you can optimize storage costs within a DWS with no change to existing queries.

 #### Hot Storage

 This is the most common storage type for a database.  It is the default storage type for data in the DWS instance.

 Storage cost is computed based on the allocated Hot storage space for the warehouse instance.  Storage is allocated to the warehouse on-demand up to the specified limit set by you.  The current limit is 4.5TB per node.  If your needs exceed 4.5TB per node, please contact us to increase your node storage limit.

 #### Warm Storage

Warm Storage provides an excellent trade-off between cost and performance.  Warm storage is ideal for data used in batch processing, infrequently accessed historical data, or other general data that does not have high performance requirements.  Warm storage provides good performance and does not have per node size limits.

 #### Cold Storage

 Cold storage is significantly less expensive than both Hot and Warm but it does have limitations.  It is not included in the backup snapshots.  It has significantly lower performance and is generally not suitable for queries that must be responsive.

 However, for low usage or archival data it can provide a substantial cost savings while still enabling real-time access to the data, albeit at a slower query speed.  This is a significant improvement over using ETL processes to archive table data and then needing to reconstitute it later when required through additional ETL processes.

 For example, if the current and prior year financial data is stored in high performance storage to handle the vast majority of queries, prior years could be stored in Cost Optimized storage.  When access to several years is needed, exceeding what is in hot storage, then a simple UNION query of the hot data and the cold data will return the full dataset.  This eliminates complex data archival processes by keeping all the data readily available in the same DWS instance while optimizing storage costs.
 

### Network Egress

| Source Geolocation                   | Egress (per GB) |  Ingress (per GB) |
|--------------------------------------|-----------------|-------------------|
| Worldwide Locations (Default)        |           $0.13 |              Free |
| China Locations (excluding Hong Kong)|           $0.26 |              Free |
| Australia Locations                  |           $0.20 |              Free |


Network egress is calculated based on the egress traffic from your PlaidCloud Workspace.  In terms of the egress traffic from a DWS instance, traffic to PlaidCloud applications in the same region such as Analyze and Dashboard are excluded.  However, if you are connecting directly to the DWS instance through the external access point, egress charges will apply.  In addition, if you access DWS instances from different regions using PlaidCloud applications then egress charges will apply.

If you connect between DWS instances in the same region using internal network routing there are no egress charges.  However, if you connect using the external endpoint then egress charges will apply.

There is no charge for ingress traffic.


### Backup Retention Period

| Retention Period                               | Hourly Cost (GB/hr) |  Monthly Cost (GB/month)  |
|------------------------------------------------|---------------------|---------------------------|
| Scheduled Backups - First 30 Days              |                Free |                      Free |
| Scheduled Backups - Retention (after 30 days)  |           $0.000274 |                     $0.02 |
| On-Demand Backup Snapshots                     |           $0.000274 |                     $0.02 |


By default, all scheduled backups are stored for 30 days free of charge.  Setting the retention period beyond 30 days will incur additional storage retention charges.  Backup retention storage cost is based on the allocated storage size of the DWS instance when the backup was taken and the duration for which you would like to retain each backup beyond 30 days.

For example, if the DWS instance allocated storage is 200GB and the additional retention period is 7 days, the backup storage cost is computed as 200GB x 7 Days = 1,400 GB Days.

1,400 GB days x 24 hours/day x $0.000274 per GB/hr = $9.20

On-demand backups can be taken at any time and will incur backup storage fees immediately.  There is a minimum of 30 days billing applied to on-demand backups even if they are deleted within the 30 days.

By default, on-demand backups do not have a retention period set.  If you make on-demand backups without a retention period, you must manually delete the backup or backup storage fees will continue to accrue.

If you put a hold on a backup to prevent deletion when the retention period expires, you must remove that hold or manually delete the backup.  If the hold remains you will continue to incur backup storage fees. 

## Premium Capabilities Included

PlaidCloud DWS provides several additional features as part of each DWS instance that provide valuable capabilities without additional fees.  Each DWS instance includes [MADLib](https://madlib.apache.org/), [PostGIS](https://postgis.net/), and [PXF](https://github.com/greenplum-db/pxf).

The [MADLib](https://madlib.apache.org/) and [PostGIS](https://postgis.net/) libraries allow you to perform machine learning and geospatial analysis without moving your data or using other external tools.  [PXF](https://github.com/greenplum-db/pxf) provides the ability to query external data files, whose metadata is not managed by the database. PXF includes built-in connectors for accessing data that exists inside HDFS files, Hive tables, HBase tables, JDBC-accessible databases and more. Users can also create their own connectors to other data storage or processing engines.
