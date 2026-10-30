---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — WKT 문자열로 선 지오메트리를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

WKT 문자열로 선 지오메트리를 만듭니다.

## Analyze 구문

```python
func.st_linefromtext(<wkt>)
```

## Analyze 예제

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 구문

```sql
ST_LINEFROMTEXT(<wkt>)
```

## SQL 예제

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
