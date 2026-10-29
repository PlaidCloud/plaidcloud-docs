---
title: CURTIME (Lakehouse v2)
description: CURTIME — retorna a hora atual. Alias de `CURRENT_TIME`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

Retorna a hora atual. Alias de `CURRENT_TIME`.

## Sintaxe do Analyze

```python
func.curtime()
```

## Exemplos do Analyze

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Sintaxe SQL

```sql
CURTIME()
```

## Exemplos SQL

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
