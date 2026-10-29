---
title: ORD (Lakehouse v1)
description: ORD — zwraca kod znaku dla pierwszego znaku od lewej w ciągu (wartość ASCII dla znaków jednobajtowych, obliczona wartość dla wielobajtowych).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Jeśli pierwszy znak od lewej nie jest znakiem wielobajtowym, ORD() zwraca tę samą wartość co funkcja ASCII().

Jeśli pierwszy znak od lewej w ciągu str jest znakiem wielobajtowym, zwraca kod tego znaku,
obliczony z wartości liczbowych jego bajtów składowych według następującego wzoru:

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Składnia Analyze

```python
func.ord(<str>)
```

## Przykłady Analyze

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## Składnia SQL

```sql
ORD(<str>)
```

## Argumenty

| Argumenty | Opis         |
|-----------|--------------|
| `<str>`   | Ciąg znaków. |

## Typ zwracany

`BIGINT`

## Przykłady SQL

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
