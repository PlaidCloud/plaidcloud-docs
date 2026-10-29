---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "Verwenden Sie die Hilfsfunktion ENCODE_SORT_KEY in PlaidCloud Lakehouse. Kodiert Werte in einen binären Sortierschlüssel, der die Sortierreihenfolge erhält. Nützlich für zusammengesetzte."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

Kodiert Werte in einen binären Sortierschlüssel, der die Sortierreihenfolge erhält. Nützlich für zusammengesetzte Sortierschlüssel.

## Analyze-Syntax

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Analyze-Beispiele

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## SQL-Syntax

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## SQL-Beispiele

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
