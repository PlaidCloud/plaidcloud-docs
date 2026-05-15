---
title: Dimension Sort
description: Automatically sort dimension members in a PlaidCloud workflow step to maintain consistent ordering within your hierarchies.
sidebar:
  order: 5
---

## Description

Sorts a dimension's members under their parents — alphabetical, by value, by property, or by a custom order column. Avoids the tedium of manually dragging hierarchy members into the right order, especially useful after a bulk load or a major restructure.

Operates on the dimension in place; no source or target table is needed.


## Dimension Selection
### Specify Dimension Dynamically
If **dimensions** or **paths** were created dynamically then same variables can be used to sort them. Using variables in the sort process is useful since it eliminates the need to update the Dimension Sort step manually on a periodic basis.



An example that uses the `current_month` variable to dynamically sort the Materials dimension:

```text
/Dimensions/{current_month}/Products/Materials
```

### Use Specific Dimension

Use the dropdown menu to select a specific dimension to sort.
