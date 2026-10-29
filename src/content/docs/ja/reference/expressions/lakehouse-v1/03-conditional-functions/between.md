---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — 数値、文字列、または日付の値が、指定した範囲の内側（または外側）にある場合にtrueになります。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

指定した数値または文字列の` <expr>`が、定義された下限と上限の範囲内にある場合に、`true`を返します。

## Analyzeの構文

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyzeの例

```python
table.column.between(0, 5)
```

## SQLの構文

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQLの例

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
