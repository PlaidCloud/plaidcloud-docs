---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN — returns the result set of a previous command in same session as if the result was a table.
---

Returns the result set of a previous command in same session as if the result was a table.


## SQL Syntax

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## SQL Examples

Create a simple table:

```sql
CREATE TABLE t1(a int);
```

Insert some values;

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
