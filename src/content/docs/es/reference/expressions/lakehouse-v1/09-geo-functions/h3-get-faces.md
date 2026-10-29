---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — encuentra todas las caras del icosaedro intersecadas por el índice H3 dado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

Encuentra todas las caras del icosaedro intersecadas por el índice [H3](https://eng.uber.com/h3/) dado. Las caras se representan como números enteros del 0 al 19.

## Sintaxis de Analyze

```python
func.h3_get_faces(h3)
```

## Ejemplos de Analyze

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_GET_FACES(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
