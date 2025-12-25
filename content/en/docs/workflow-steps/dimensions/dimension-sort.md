---
title: Dimension Sort
slug: dimension-sort
weight: 5.0
description: Sort dimensions automatically
date: 2022-01-25T07:40:18
---

## Description
Sort dimensions automatically.


![Dimension Clear](/images/dimension_clear.png)



## Dimension Selection
### Specify Dimension Dynamically
If **dimensions** or **paths** were created dynamically then same variables can be used to sort them. Using variables in the sort process is useful since it eliminates the need to update the Dimension Sort step manually on a periodic basis.



An example that uses the `current_month` variable to dynamically sort the Materials dimension:

```
/Dimensions/{current_month}/Products/Materials
```

### Use Specific Dimension

Use the dropdown menu to select a specific dimension to sort.