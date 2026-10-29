---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Verwenden Sie die Zeichenfolgenfunktion SUBSTRING_INDEX in PlaidCloud Lakehouse. Gibt eine Teilzeichenfolge zurück, die vor oder nach einer angegebenen Anzahl von Vorkommen eines Trennzeichens liegt."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Gibt eine Teilzeichenfolge zurück, die vor oder nach einer angegebenen Anzahl von Vorkommen eines Trennzeichens liegt.

## Analyze-Syntax

```python
func.substring_index(<str>, <delim>, <count>)
```

## Analyze-Beispiele

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## SQL-Syntax

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## SQL-Beispiele

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
