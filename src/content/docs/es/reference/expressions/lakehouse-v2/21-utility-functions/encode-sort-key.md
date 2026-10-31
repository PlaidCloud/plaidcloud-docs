---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "Use la función de utilidad ENCODE_SORT_KEY en PlaidCloud Lakehouse. Codifica valores en una clave de ordenación binaria que conserva el orden. Es útil para claves de ordenación compuestas."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

Codifica valores en una clave de ordenación binaria que conserva el orden. Es útil para claves de ordenación compuestas.

## Sintaxis de Analyze

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Ejemplos de Analyze

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## Sintaxis de SQL

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## Ejemplos de SQL

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
