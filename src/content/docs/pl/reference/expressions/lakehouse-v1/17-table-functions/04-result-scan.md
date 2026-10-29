---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN — zwraca zbiór wyników poprzedniego polecenia z tej samej sesji tak, jakby wynik był tabelą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

Zwraca zbiór wyników poprzedniego polecenia z tej samej sesji tak, jakby wynik był tabelą.


## Składnia SQL

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## Przykłady SQL

Utwórz prostą tabelę:

```sql
CREATE TABLE t1(a int);
```

Wstaw kilka wartości;

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
