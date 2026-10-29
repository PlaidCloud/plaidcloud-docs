---
title: BAR (Lakehouse v2)
description: "Verwenden Sie die Hilfsfunktion BAR in PlaidCloud Lakehouse. Gibt eine visuelle Balkendarstellung eines Werts innerhalb eines Bereichs als Zeichenfolge zurück. Nützlich für textbasierte."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Gibt eine visuelle Balkendarstellung eines Werts innerhalb eines Bereichs als Zeichenfolge zurück. Nützlich für textbasierte Visualisierungen.

## Analyze-Syntax

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Analyze-Beispiele

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## SQL-Syntax

```sql
BAR(<value>, <min>, <max>, <width>)
```

## SQL-Beispiele

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
