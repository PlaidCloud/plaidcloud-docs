---
title: Dimension Clear
slug: dimension-clear
weight: 1.0
description: Clears the contents of a dimension including structure, values, aliases, properties, and alternate hierarchies
date: 2022-01-25T07:40:18
---
## Description
Clears the contents of a dimension including structure, values, aliases, properties, and alternate hierarchies


![Dimension Clear](/images/dimension_clear.png)



## Dimension Selection
### Specify Dimension Dynamically
If **dimensions** or **paths** were created dynamically then same variables can be used to clear them. Using variables in the clear process is useful since it eliminates the need to update the Dimension Clear step manually on a periodic basis.



An example that uses the `current_month` variable to dynamically clear the Materials dimension:

```
/Dimensions/{current_month}/Products/Materials
```

### Use Specific Dimension

Use the dropdown menu to select a specific dimension to clear.

