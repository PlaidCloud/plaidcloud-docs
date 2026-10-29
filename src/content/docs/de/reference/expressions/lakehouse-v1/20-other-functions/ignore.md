---
title: IGNORE (Lakehouse v1)
description: IGNORE ignoriert bei einer INSERT-IGNORE-Anweisung die Zeilen mit ungültigen Daten, die den Fehler verursachen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

Bei einer INSERT-IGNORE-Anweisung werden die Zeilen mit ungültigen Daten, die den Fehler verursachen, ignoriert, und die Zeilen mit gültigen Daten werden in die Tabelle eingefügt.

## SQL-Syntax

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
