---
title: REGEXP (Lakehouse v1)
description: REGEXP — 문자열 <expr>이 <pattern>으로 지정한 정규식과 일치하면 true를, 그렇지 않으면 false를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

문자열 `<expr>`이 `<pattern>`으로 지정한 정규식과 일치하면 `true`를, 그렇지 않으면 `false`를 반환합니다.

## Analyze 구문

```python
<column>.regexp_match(<pattern>)
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

my_clothes.regexp_match('p*')
┌───────────────────────────────┐
│ my_clothes.regexp_match('p*') │
├───────────────────────────────┤
│ true                          │
│ true                          │
│ true                          │
│ false                         │
└───────────────────────────────┘
```

## SQL 구문

```sql
<expr> REGEXP <pattern>
```

## 별칭

- [RLIKE](../rlike)

## SQL 예제

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
