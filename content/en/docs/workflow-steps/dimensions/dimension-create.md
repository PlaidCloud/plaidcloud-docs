---
title: Dimension Create
slug: dimension-create
description: Creates a dimension for use and loading
date: 2022-01-25T07:40:18
---


![Dimension Create](/images/dimension_create.png)

## Dimension To Create
### Name
You can either use a specific name for the dimension to be created or include variables for dynamic naming.


Variables is useful when dimensions are updated on a periodic basis and retaining the historical view is desired.

An example that uses the `current_month` variable to dynamically name the dimension:

```
dimension_name_{current_month}
```
### Path
Paths let you create folder structures that the dimensions are are stored in. You can use variables here as well to make the folder structure dynamic.
An example that uses the `current_month` variable to dynamically name a folder:

```
/Dimensions/{current_month}/Product/
```

### Memo
The Memo field is used a place to store comments or notes.