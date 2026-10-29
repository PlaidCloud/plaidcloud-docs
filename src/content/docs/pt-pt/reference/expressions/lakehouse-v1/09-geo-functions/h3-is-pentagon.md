---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — verifica se o índice H3 indicado representa uma célula pentagonal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

Verifica se o índice [H3](https://eng.uber.com/h3/) indicado representa uma célula pentagonal. 

## Sintaxe do Analyze

```python
func.h3_is_pentagon(h3)
```

## Exemplos do Analyze

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_IS_PENTAGON(h3)
```

## Exemplos de SQL

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
