---
title: RAND(n) (Lakehouse v1)
description: RAND(n) – gibt einen zufälligen Gleitkommawert v im Bereich 0 &lt;= v &lt; 1.0 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

Gibt einen zufälligen Gleitkommawert v im Bereich 0 &lt;= v &lt; 1.0 zurück. Um eine zufällige ganze Zahl R im Bereich i &lt;= R &lt; j zu erhalten, verwenden Sie den Ausdruck FLOOR(i + RAND() * (j − i)). Das Argument `n` dient als Seed-Wert. Bei gleichen Argumentwerten gibt RAND(n) jedes Mal denselben Wert zurück und erzeugt so eine wiederholbare Folge von Spaltenwerten.

## Analyze-Syntax

```python
func.rand( <n>)
```

## Analyze-Beispiele

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## SQL-Syntax

```sql
RAND( <n>)
```

## SQL-Beispiele

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
