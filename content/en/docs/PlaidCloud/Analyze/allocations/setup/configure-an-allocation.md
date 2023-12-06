---
title: Configure an Allocation
slug: configure-an-allocation
weight: 1.0
description: Set up a cost allocation transform and manage assignments
date: 2022-01-25T07:40:20
---


## Purpose

Allocations enable values (typically costs) to be shredded to a more-granular level by applying a driver. Allocations are used to for a multitude of purposes. including but not limited to **Activity-Based Costing**, **IT & Shared Service Chargeback**, calculation of fully loaded cost to produce and provide a good or service to customers, etc. They are a fundamental tool for financial analysis, and a cornerstone for managerial reporting operations such as **Customer & Product Profitability**. They are also a useful construct for establishing and managing global Intercompany Transfer Prices for goods and services.

## Setting up the Allocation transform

From a practical purpose, allocations are set up in PlaidCloud in similar fashion as other data transforms such as joins and lookups. Four configuration parameters must be set in order for an Allocation transform to succeed.

1. **Specify Preallocated Data**: Specify the preallocated data table in the **Values To Allocate Table** section of the allocation transform.
2. **Specify Driver Data**: Driver data will serve as the basis for the ratios used in the allocation. Choose the driver data table in the **Driver Data Table** section of the allocation transform.
3. **Specify the Results Table**: Post-allocated data must be stored in a table. Specify the table in the **Allocation Result Table** section of the allocation result section of the transform.
4. **Specify the Assignment Dimension**: Allocations require an assignment dimension, whose purpose is to provide the prescription for how each record or set of records in the preallocated will be assigned. Specify the the assignment dimension in the **Assignment Dimension Hierarchy** section of the allocation transform.

## Key Concepts

The sum of values in an allocated dataset should tie out to those of the pre-allocated source data

Allocations are accessible in PlaidCloud as a transform option. To set up an allocation, first, set up assignments, and then configure an allocation transform to use the assignments to allocate inbound records using a specified driver table.

Assignments are special dimensions. They are accessed within the Dimensions section of a PlaidCloud Project.

To set up an assignment dimension, perform the following steps:

1. From the project screen, Navigate to the Dimensions tab
2. Create a new dimension
