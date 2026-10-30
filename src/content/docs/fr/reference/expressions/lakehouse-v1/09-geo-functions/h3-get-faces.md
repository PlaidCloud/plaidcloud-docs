---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — trouve toutes les faces de l'icosaèdre croisées par l'index H3 donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

Trouve toutes les faces de l'icosaèdre croisées par l'index [H3](https://eng.uber.com/h3/) donné. Les faces sont représentées par des entiers de 0 à 19.

## Syntaxe Analyze

```python
func.h3_get_faces(h3)
```

## Exemples Analyze

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
H3_GET_FACES(h3)
```

## Exemples SQL

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
