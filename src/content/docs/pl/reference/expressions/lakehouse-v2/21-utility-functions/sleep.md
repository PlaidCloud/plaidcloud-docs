---
title: SLEEP (Lakehouse v2)
description: SLEEP — wstrzymuje wykonanie na podaną liczbę sekund. Po powodzeniu zwraca 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Wstrzymuje wykonanie na podaną liczbę sekund. Po powodzeniu zwraca 0.

## Składnia Analyze

```python
func.sleep(<seconds>)
```

## Przykłady Analyze

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## Składnia SQL

```sql
SLEEP(<seconds>)
```

## Przykłady SQL

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
