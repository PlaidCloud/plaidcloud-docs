---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — cria uma geometria de linha a partir de uma string WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

Cria uma geometria de linha a partir de uma string WKT.

## Sintaxe do Analyze

```python
func.st_linefromtext(<wkt>)
```

## Exemplos do Analyze

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxe SQL

```sql
ST_LINEFROMTEXT(<wkt>)
```

## Exemplos de SQL

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
