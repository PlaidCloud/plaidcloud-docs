---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN — renvoie le jeu de résultats d'une commande précédente de la même session, comme si ce résultat était une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

Renvoie le jeu de résultats d'une commande précédente de la même session, comme si ce résultat était une table.


## Syntaxe SQL

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## Exemples SQL

Créez une table simple :

```sql
CREATE TABLE t1(a int);
```

Insérez quelques valeurs ;

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
