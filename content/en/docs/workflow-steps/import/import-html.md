---
title: Import HTML
slug: import-html
weight: 9.0
description: Import HTML table data from the internet
date: 2022-01-25T07:39:57
---

## Description

Import HTML table data from the internet.


## Examples

No examples yet...

---

## Unique Configuration Items

### Select Tables in HTML

Since it is possible to have multiple tables on a web page, the user must specify which table to import. To do so, specify **Name** and/or **Attribute** values to match.

For example, consider the following table:

```html
<table border="1" id="import"> <tr> <th>Hello</th><th>World</th> </tr> <tr> <td>1</td><td>2</td> </tr> <tr> <td>3</td><td>4</td> </tr> </table>
```

To import this table, specify *id:import* in the **Name Match** field.

Additionally, there is an option to skip rows at the beginning of the table.


### Column Headers

Specify the row to use for header information. By default, the **Column Header Row** is 0.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
