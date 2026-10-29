---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — crée une géométrie de ligne à partir d'une chaîne WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

Crée une géométrie de ligne à partir d'une chaîne WKT.

## Syntaxe Analyze

```python
func.st_linefromtext(<wkt>)
```

## Exemples Analyze

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Syntaxe SQL

```sql
ST_LINEFROMTEXT(<wkt>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
