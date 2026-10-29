---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — converte a representação do índice H3 informado em sua representação de string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

Converte a representação do índice [H3](https://eng.uber.com/h3/) informado em sua representação de string. 

## Sintaxe do Analyze

```python
func.h3_to_string(h3)
```

## Exemplos do Analyze

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_TO_STRING(h3)
```

## Exemplos de SQL

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
