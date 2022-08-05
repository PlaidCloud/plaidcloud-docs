---
title: Dimension Delete
slug: dimension-delete
description: Deletes a dimension along with all associated structure, values, properties, aliases, and alternate hierarchies
date: 2022-01-25T07:40:18
---


## Description
Deletes a dimension along with all associated structure, values, properties, aliases, and alternate hierarchies


![Dimension Clear](/images/dimension_clear.png)



## Dimension Selection
### Specify Dimension Dynamically
If **dimensions** or **paths** were created dynamically then same variables can be used to delete them. Using variables in the delete process is useful since it eliminates the need to update the Dimension Delete step manually on a periodic basis.



An example that uses the `current_month` variable to dynamically delete the Materials dimension:

```
/Dimensions/{current_month}/Products/Materials
```

### Use Specific Dimension

Use the dropdown menu to select a specific dimension to delete.
