---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — sprawdza, czy podany indeks H3 reprezentuje komórkę pięciokątną.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

Sprawdza, czy podany indeks [H3](https://eng.uber.com/h3/) reprezentuje komórkę pięciokątną. 

## Składnia Analyze

```python
func.h3_is_pentagon(h3)
```

## Przykłady Analyze

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_IS_PENTAGON(h3)
```

## Przykłady SQL

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
