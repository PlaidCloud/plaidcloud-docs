---
title: H3_GET_FACES
---

Finds all icosahedron faces intersected by the given [H3](https://eng.uber.com/h3/) index. Faces are represented as integers from 0-19.

## Analyze Syntax

```python
func.h3_get_faces(h3)
```

## Analyze Examples

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_FACES(h3)
```

## SQL Examples

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```