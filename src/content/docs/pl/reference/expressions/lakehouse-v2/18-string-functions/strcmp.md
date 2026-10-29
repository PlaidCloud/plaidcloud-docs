---
title: STRCMP (Lakehouse v2)
description: "Użyj funkcji tekstowej STRCMP w PlaidCloud Lakehouse. Porównuje dwa ciągi leksykograficznie. Zwraca 0, jeśli są równe, -1, jeśli str1 < str2, oraz 1, jeśli str1 > str2."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

Porównuje dwa ciągi leksykograficznie. Zwraca 0, jeśli są równe, -1, jeśli str1 &lt; str2, oraz 1, jeśli str1 > str2.

## Składnia Analyze

```python
func.strcmp(<str1>, <str2>)
```

## Przykłady Analyze

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## Składnia SQL

```sql
STRCMP(<str1>, <str2>)
```

## Przykłady SQL

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
