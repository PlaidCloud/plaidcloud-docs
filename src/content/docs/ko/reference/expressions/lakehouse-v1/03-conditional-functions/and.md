---
title: AND (Lakehouse v1)
description: AND — 조건부 AND 연산자입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

조건부 AND 연산자입니다. 두 조건이 모두 참인지 확인합니다.

## Analyze 구문

```python
and_(<expr1>[, <expr2> ...])
```

## Analyze 예제

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL 구문

```sql
<expr1> AND <expr2>
```

## SQL 예제

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
