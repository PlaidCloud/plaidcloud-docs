---
title: Pricing
description: PlaidCloud Data Lakehouse Service Pricing
weight: 2.0
date: 2022-01-25T07:39:51
---


## Usage Based

The cost of a PlaidCloud Data Lakehouse instance is determined by a limited number of factors that you control.  All costs incurred are usage based.

The factors that impact cost are:
 - Concurrency Factor - The size of each compute node in your warehouse instance
 - Parallelism Factor - The number of nodes in your warehouse instance
 - Allocated Storage - The number of Gigabytes of storage consumed by your warehouse instance
 - Network Egress - The number of Gigabytes of network egress. Excludes traffic to PlaidCloud applications within the same region.  Ingress is always free.
 - Time Travel Period - How many days, weeks, or months to retain time travel history on tables

Storage, backups, and network egress are calculated in gigabytes (GB), where 1 GB is 2^30 bytes. This unit of measurement is also known as a [gibibyte (GiB)](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units).

All prices are in USD.  If you are paying in another currency please convert to your currency using the appropriate rate.

Billing is on an hourly basis.  The monthly prices shown are illustrative based on a 730 hour month.


## Controlling Factors

### Concurrency Factor

| Compute Type     | Hourly Cost (streams/hr) |  Monthly Cost (streams/month) |
|------------------|--------------------------|-------------------------------|
| Standard         |               Contact Us |                  Contact Us   |

Concurrency determines how many simultaneous queries are handled by the DLS instance.  This is expressed as a number of process streams.  There is not a 1:1 relationship between streams and query capacity since a single stream can handle multiple simultaneous queries.  However, as the number of concurrent requests increase, the query duration may exceed the desired response time and an increase in the concurrency factor will help.

From a conceptual standpoint you can view processing streams as vCPUs used to process queries.

The default concurrency factor is 2, which is a good starting point if you are unsure of your needs.  It can be adjusted from 1 to 14.  If your needs exceed 14, please contact us to increase your concurrency limit.


### Parallelism Factor

There is no additional cost per node.  The compute cost of the DLS instance is the product of concurrency and parallelism plus the master node.

Parallelism determines how many nodes are in the DLS instance.  This is expressed as node count.  The number of nodes determines how much compute power can be applied to any single query.  By increasing the node count, the computational part of the query can be spread out over many process streams.  In addition, the storage throughput is multiplied by the number of nodes, which is very valuable when dealing with large datasets.

For example, if the maximum theoretical write throughput of a single node was 4 TB/sec, a warehouse with 8 nodes would have a theoretical write throughput of 8 x 4 TB/sec = 32 TB/sec.  There are many factors that impact write speed including compression level, indexes, table storage type, network overhead, etc... but in general, nodes apply a multiplying factor to data throughput speed.


### Allocated Storage

Three types of table storage options are available in a PlaidCloud DLS:
 - Regional
 - Multi-Regional

| Storage Type     | Hourly Cost (GB/hr) |  Monthly Cost (GB/month)  |
|------------------|---------------------|---------------------------|
| Regional         |          Contact Us |              Contact Us   |
| Multi-Regional   |          Contact Us |              Contact Us   |

 #### Regional

 The storage provides triple redundancy across multiple availability zones in a single region.  This is suitable for most workloads that do not need geographically distributed redundancy.

 #### Multi-Regional

This storage provides triple redundancy in each region and is stored in two regions.  This provides geographical redundancy and fast failover for data requiring the highest availability.
 

### Network Egress

Network Egress and Ingress charges are dependent on the cloud provider, region, and destination for the traffic.  Contact us and we can provide a detailed cost matrix.

Network egress is calculated based on the egress traffic from your PlaidCloud Workspace.  In terms of the egress traffic from a DLS instance, traffic to PlaidCloud applications in the same region such as Analyze and Dashboard are excluded.  However, if you are connecting directly to the DLS instance through the external access point, egress charges will apply.  In addition, if you access DLS instances from different regions using PlaidCloud applications then egress charges will apply.

If you connect between DLS instances in the same region using internal network routing there are no egress charges.  However, if you connect using the external endpoint then egress charges will apply.

There is no charge for ingress traffic.
