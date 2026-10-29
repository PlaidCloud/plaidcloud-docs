---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — crea una geometría de línea a partir de una cadena WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

Crea una geometría de línea a partir de una cadena WKT.

## Sintaxis de Analyze

```python
func.st_linefromtext(<wkt>)
```

## Ejemplos de Analyze

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxis de SQL

```sql
ST_LINEFROMTEXT(<wkt>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
