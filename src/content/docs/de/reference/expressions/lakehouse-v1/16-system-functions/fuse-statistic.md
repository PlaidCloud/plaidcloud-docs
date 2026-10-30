---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC gibt die geschätzte Anzahl eindeutiger Werte jeder Spalte einer Tabelle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

Gibt die geschätzte Anzahl eindeutiger Werte jeder Spalte einer Tabelle zurück.


## SQL-Syntax

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## SQL-Beispiele

Sie verwenden diese Funktion höchstwahrscheinlich zusammen mit `ANALYZE TABLE <table_name>`, um die statistischen Informationen einer Tabelle zu erzeugen und zu prüfen. Weitere Erläuterungen und Beispiele finden Sie unter OPTIMIZE TABLE.
