---
title: SLEEP (Lakehouse v2)
description: SLEEP — hält die Ausführung für die angegebene Anzahl von Sekunden an. Gibt bei Erfolg 0 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Hält die Ausführung für die angegebene Anzahl von Sekunden an. Gibt bei Erfolg 0 zurück.

## Analyze-Syntax

```python
func.sleep(<seconds>)
```

## Analyze-Beispiele

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## SQL-Syntax

```sql
SLEEP(<seconds>)
```

## SQL-Beispiele

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
