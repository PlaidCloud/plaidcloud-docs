---
title: Loading and Unloading Dimensions
slug: loading
description: Load dimensions from and unload to tables
date: 2022-01-25T07:39:48
weight: 3.0
---

Dimensions can be maintained from workflow operations by loading data.  In addition, dimensional data can be flattened into tabular data and stored in tables.  This is often useful for enriching reporting and analytics data.


## Loading Dimensions

Since dimensions represent hierarchical data structures, the load process must convey the relationships in the data.  PlaidCloud supports two different data structures for loading dimensions:
 * Parent-Child - The data is organized vertically with a *Parent* column and *Child* column defining each parent of a child throughout the structure
 * Levels - The data is organized horizontally with each column representing a level in the hierarchy from left to right

 In addition to structure, other dimension information can be included in the load process such as values, aliases, and properties.

 See the Workflow Step for [Dimension Load](/docs/workflow-steps/dimensions/dimension-load) for more information.


## Unloading (Exporting) Dimensions

Exporting dimensions to tables supports two structural approaches:
 * Parent-Child - The data is organized vertically with a *Parent* column and *Child* column defining each parent of a child throughout the structure
 * Levels - The data is organized horizontally with each column representing a level in the hierarchy from left to right

Properties and values can also be included in the flattened tabular data.

 See the Workflow Step for [Dimension Unload](/docs/workflow-steps/dimensions/dimension-unload) for more information.