---
title: Dimension Create
description: Create a new hierarchical dimension in a PlaidCloud workflow step to organize and structure your data classification system.
sidebar:
  order: 2
---

## Description
Creates a dimension for use and loading


![Dimension Create](/images/dimension_create.png)

## Dimension to Create
### Name
You can either use a specific name for the dimension to be created or include variables for dynamic naming.


Variables are useful when dimensions are updated on a periodic basis and retaining the historical view is desired.

An example that uses the `current_month` variable to dynamically name the dimension:

```text
dimension_name_{current_month}
```
### Path
Paths let you create folder structures that the dimensions are are stored in. You can use variables here as well to make the folder structure dynamic.
An example that uses the `current_month` variable to dynamically name a folder:

```text
/Dimensions/{current_month}/Product/
```

### Memo
The Memo field is used a place to store comments or notes.
