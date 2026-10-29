---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — encontra todas as faces do icosaedro que o índice H3 informado intersecta.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

Encontra todas as faces do icosaedro que o índice [H3](https://eng.uber.com/h3/) informado intersecta. As faces são representadas como inteiros de 0 a 19.

## Sintaxe do Analyze

```python
func.h3_get_faces(h3)
```

## Exemplos do Analyze

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_GET_FACES(h3)
```

## Exemplos de SQL

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
