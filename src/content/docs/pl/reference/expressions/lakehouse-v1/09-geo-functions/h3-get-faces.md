---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — wyszukuje wszystkie ściany dwudziestościanu przecinane przez podany indeks H3.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

Wyszukuje wszystkie ściany dwudziestościanu przecinane przez podany indeks [H3](https://eng.uber.com/h3/). Ściany są reprezentowane jako liczby całkowite z zakresu 0–19.

## Składnia Analyze

```python
func.h3_get_faces(h3)
```

## Przykłady Analyze

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_GET_FACES(h3)
```

## Przykłady SQL

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
