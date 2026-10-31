---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — retorna o fuso horário atual da sessão.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

Retorna o fuso horário atual da sessão.

## Sintaxe do Analyze

```python
func.current_timezone()
```

## Exemplos do Analyze

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## Sintaxe SQL

```sql
CURRENT_TIMEZONE()
```

## Exemplos SQL

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
