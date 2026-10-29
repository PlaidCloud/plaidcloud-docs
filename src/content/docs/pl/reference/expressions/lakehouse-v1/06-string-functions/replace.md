---
title: REPLACE (Lakehouse v1)
description: REPLACE — zwraca ciąg znaków str, w którym wszystkie wystąpienia ciągu from_str zastąpiono ciągiem to_str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

Zwraca ciąg znaków str, w którym wszystkie wystąpienia ciągu from_str zastąpiono ciągiem to_str.

## Składnia Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Przykłady Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## Składnia SQL

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Argumenty

| Argumenty    | Opis                       |
|--------------|----------------------------|
| `<str>`      | Ciąg znaków.               |
| `<from_str>` | Ciąg zastępowany.          |
| `<to_str>`   | Ciąg zastępujący.          |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
