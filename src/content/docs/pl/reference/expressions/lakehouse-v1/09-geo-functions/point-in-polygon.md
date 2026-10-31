---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — oblicza, czy dany punkt leży wewnątrz wielokąta utworzonego przez połączenie punktów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

Oblicza, czy dany punkt leży wewnątrz wielokąta utworzonego przez połączenie wielu punktów. Wielokąt jest kształtem zamkniętym, łączącym pary współrzędnych w kolejności ich występowania. Zmiana kolejności par współrzędnych może dać inny kształt.

## Składnia Analyze

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Przykłady Analyze

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Przykłady SQL

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
