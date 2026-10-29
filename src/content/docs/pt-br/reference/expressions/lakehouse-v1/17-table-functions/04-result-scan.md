---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN — retorna o conjunto de resultados de um comando anterior da mesma sessão como se o resultado fosse uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

Retorna o conjunto de resultados de um comando anterior da mesma sessão como se o resultado fosse uma tabela.


## Sintaxe SQL

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## Exemplos de SQL

Crie uma tabela simples:

```sql
CREATE TABLE t1(a int);
```

Insira alguns valores;

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
