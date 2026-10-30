---
title: INSTR (Lakehouse v1)
description: INSTR — zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str.
Działa tak samo jak dwuargumentowa postać funkcji LOCATE(), z tą różnicą, że kolejność argumentów jest odwrócona.

## Składnia Analyze

```python
func.instr(<str>, <substr>)
```

## Przykłady Analyze

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## Składnia SQL

```sql
INSTR(<str>, <substr>)
```

## Argumenty

| Argumenty  | Opis         |
|------------|--------------|
| `<str>`    | Ciąg znaków. |
| `<substr>` | Podciąg.     |

## Typ zwracany

`BIGINT`

## Przykłady SQL

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
