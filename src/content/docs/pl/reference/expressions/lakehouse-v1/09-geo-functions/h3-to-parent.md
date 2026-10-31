---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — zwraca indeks nadrzędny zawierający h3 w rozdzielczości parent_res.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

Zwraca indeks nadrzędny zawierający `h3` w rozdzielczości `parent_res`. Zwrócenie wartości 0 oznacza wystąpienie błędu.

## Składnia Analyze

```python
func.h3_to_parent(h3, parent_res)
```

## Przykłady Analyze

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_TO_PARENT(h3, parent_res)
```

## Przykłady SQL

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
