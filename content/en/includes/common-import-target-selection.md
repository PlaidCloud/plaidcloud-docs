---
title: File Import Target Table Selection
---

### Target Table

The target selection for imports is limited to tables only since views do not contain underlying data.

#### Dynamic Option

The Dynamic option allows specification of a table using text, including variables.  This is useful when employing
variable driven workflows where table and view references are relative to the variables specified.

An example that uses the `current_month` variable to dynamically point to target table:

```
legal_entity/inputs/{current_month}/ledger_values
```

{{< note >}}
If the table does not exist it will be created dynamically when the import process runs
{{< /note >}}

#### Static Option

When a specific table is desired as the target for the import, leave the *Dynamic* box unchecked and select the target Table.

If the target Table does not exist, select the *Create new table* button to create the table in the desired location.

Table Explorer is always avaible with any table selection.  Click on the Table Explorer button to the right of the table selection and a Table Explorer window will open.
