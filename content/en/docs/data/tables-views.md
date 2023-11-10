---
title: Using Tables and Views
slug: tables-views
description: Using and managing tables and views
date: 2022-01-25T07:39:48
weight: 2.0
---


Tabular data and information in PlaidCloud is stored in Greenplum data warehouses.  This provides massive
scalability and performance while using well understood and mature technology to minimize risk of data loss 
or corruption.

In addition, utilizing a data warehouse that operates with a common syntax allows 3rd party tools to connect
and explore data directly.  Essentially, this makes the PlaidCloud data ecosystem open and explorable while 
also ensuring industry leading security and access controls.

## Tables

Tables hold the physical tabular data throughout PlaidCloud.  Individual tables can hold many terabytes of data if needed.  Data is stored across many
physical servers and is automatically mirrored to ensure data integrity and high availability.

Tables consist of columns of various data types.  Using an appropriate data type can help with performance and especially the storage size of your data.
PlaidCloud can do a better job of compressing the data if the data is using the most appropriate data type too.  This is usually guessed by PlaidCloud but
it is also possible to change the data types using the column mappers in workflow steps.

## Views

Views act just like tables but don't hold any physical data.  They are logical representations of tables derived through a query.  Using views can save on storage.

There are some limitations to the use of views though.  Just be aware of the following:

 * View Stacking Performance - View stacking (view of a view of a view...etc) can impact performance on very large tables or complex calculations.  It might be necessary to create intermediate tables to improve performance.
 * Dashboard Performance - While perfectly fine to publish a view for Dashboard use, for very large tables you may want to publish a table rather than a view for optimal user experience.
 * Dynamic Data - The data in a view changes when the underlying referenced table data changes.  This can be both a benefit (everything updates automatically) or an unexpected headache if the desire was a static set of data.

{{< note >}}
Using views can help speed up workflows since no data movement is necessary at workflow run time.
{{< /note >}}

{{< note >}}
Since views contain no data, you will notice that they cannot be used as a target for imports.  A table must be used in that case.
{{< /note >}}
