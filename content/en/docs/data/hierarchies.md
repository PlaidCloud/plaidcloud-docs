---
title: Using Dimensions (Hierarchies)
slug: hierarchies
description: Using and managing hierarchical data
date: 2022-01-25T07:39:48
weight: 3.0
---


PlaidCloud natively manages dimension (i.e. hierarchical) data through our proprietary hierarchy storage system.  We decided to construct our own from purpose-built solution because other commercial and open-source solutions seem to present limitations that were not easily overcome.

The hierarchy storage supports not only hierarchical relationships but also properties, aliases, attributes, and values.  It is also designed to operate on large
structures and perform operations quickly including complex branch and leaf navigation.

Dimensions are managed in the `Dimensions` tab within each PlaidCloud project configuration area.


## Main Hierarchy

Each dimension (i.e. hierarchical dataset) always consists of a `main` hierarchy.  Every member of the hierarchy is represented here.

Having a `main` hierarchy helps establish the complete set of leaf nodes in the dimension.


## Alternate or Attribute Hierarchies

Alternate hierarchies are different representations of the `main` hierarchy leaf nodes.  Alternate hierarchies can consist of a subset of both
leaf nodes and roll-up (i.e. folders) in the `main` hierarchy as well as its own set of unique roll-ups.

This provides for the maximum amount of flexibility by automatically updating alternate hierarchies when children of a roll-up change or to 
strictly control the alternate hierarchy members by specifying only the leaf nodes required.

{{< note >}}
Items in the `main` hierarchy have attribute labels showing alternate hierarchies for which they also belong
{{< /note >}}

## Managing Dimensions

### Creating a Dimension

From the `New` button in the toolbar, select `New Dimension`. Enter in the desired name, directory, and a descriptive memo.

Once you press the `Create` button the dimension will be created and ready for immediate use.

You can also create a dimension from a workflow using the [Dimension Create](/docs/workflow-steps/dimensions/dimension-create) workflow step.

### Deleting a Dimension

To delete an existing dimension, select the dimension record and open the `Actions` menu in the upper right.  Select `Delete Dimension`.

This will delete the dimension and all underlying data.

You can also delete a dimension from a workflow using the [Dimension Delete](/docs/workflow-steps/dimensions/dimension-delete) workflow step.

It is also possible to clear the dimension of all structure, values, aliases, properties, and alternate hierarchies without deleting the dimension 
by using the [Dimension Clear](/docs/workflow-steps/dimensions/dimension-clear) workflow step.

### Copying a Dimension

To copy an existing dimension, select the dimension record and open the `Actions` menu in the upper right.  Select `Copy Dimension`.

This will open a dialog where you can specify the name of the copy.  Click the `Create Copy` button to make a copy of the dimension 
including values, aliases, properties, and alternate hierarchies.

### Sorting a Dimension

The dimension management area makes it easy to move hierarchy members up and down as well as changing parents.  It also makes it easy to create and delete members.

However, it can get tedious when manually moving hierarchy items around so you can sort a dimension from a workflow using the [Dimension Sort](/docs/workflow-steps/dimensions/dimension-sort) workflow step.  This can be a big time saver especially after data loads or major changes.


## Loading Dimensions

Since dimensions represent hierarchical data structures, the load process must convey the relationships in the data.  PlaidCloud supports two 
different data structures for loading dimensions:
 * Parent-Child - The data is organized vertically with a *Parent* column and *Child* column defining each parent of a child throughout the structure
 * Levels - The data is organized horizontally with each column representing a level in the hierarchy from left to right

 In addition to structure, other dimension information can be included in the load process such as values, aliases, and properties.

 See the Workflow Step for [Dimension Load](/docs/workflow-steps/dimensions/dimension-load) for more information.
