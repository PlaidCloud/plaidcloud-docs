---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — konwertuje reprezentację podanego indeksu H3 na reprezentację tekstową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

Konwertuje reprezentację podanego indeksu [H3](https://eng.uber.com/h3/) na reprezentację tekstową. 

## Składnia Analyze

```python
func.h3_to_string(h3)
```

## Przykłady Analyze

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_TO_STRING(h3)
```

## Przykłady SQL

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
