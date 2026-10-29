---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "Use a função utilitária ENCODE_SORT_KEY no PlaidCloud Lakehouse. Codifica valores em uma chave de ordenação binária que preserva a ordem de classificação. Útil para chaves compostas."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

Codifica valores em uma chave de ordenação binária que preserva a ordem de classificação. Útil para chaves de ordenação compostas.

## Sintaxe do Analyze

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Exemplos do Analyze

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## Sintaxe SQL

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## Exemplos de SQL

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
