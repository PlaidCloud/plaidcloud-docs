---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN gibt die Ergebnismenge eines vorherigen Befehls in derselben Sitzung zurück, als wäre das Ergebnis eine Tabelle.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

Gibt die Ergebnismenge eines vorherigen Befehls in derselben Sitzung zurück, als wäre das Ergebnis eine Tabelle.


## SQL-Syntax

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## SQL-Beispiele

Erstellen Sie eine einfache Tabelle:

```sql
CREATE TABLE t1(a int);
```

Fügen Sie einige Werte ein:

```sql
INSERT INTO t1(a) VALUES (1), (2), (3);
```

### `result_scan`


```bash
SELECT * FROM t1 ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```


```bash
SELECT * FROM RESULT_SCAN(LAST_QUERY_ID()) ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```
