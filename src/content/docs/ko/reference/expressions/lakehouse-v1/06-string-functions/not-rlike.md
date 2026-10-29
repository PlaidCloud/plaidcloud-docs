---
title: NOT RLIKE (Lakehouse v1)
description: NOT RLIKE — 문자열 expr이 패턴 pat로 지정한 정규식과 일치하지 않으면 1을, 그렇지 않으면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-rlike.md
---

문자열 expr이 패턴 pat로 지정한 정규식과 일치하지 않으면 1을, 그렇지 않으면 0을 반환합니다.

## Analyze 구문

```python
not_(<column>.regexp_match(<pattern>))
```

## Analyze 예제

```python

With an input table of:
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
│ shoes           │
└─────────────────┘

not_(my_clothes.regexp_match('p*'))
┌─────────────────────────────────────┐
│ not_(my_clothes.regexp_match('p*')) │
├─────────────────────────────────────┤
│ false                               │
│ false                               │
│ false                               │
│ true                                │
└─────────────────────────────────────┘
```

## SQL 구문

```sql
<expr> NOT RLIKE <pattern>
```

## SQL 예제

```sql
SELECT 'databend' not rlike 'd*';
┌─────────────────────────────┐
│ ('databend' not rlike 'd*') │
├─────────────────────────────┤
│                           0 │
└─────────────────────────────┘
```
