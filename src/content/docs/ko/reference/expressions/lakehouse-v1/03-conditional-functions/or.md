---
title: OR (Lakehouse v1)
description: OR — 조건부 OR 연산자입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

조건부 OR 연산자입니다.  두 조건 중 하나라도 참인지 확인합니다.

## Analyze 구문

```python
or_(<expr1>[, <expr2> ...])
```

## Analyze 예시

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL 구문

```sql
<expr1> OR <expr2>
```

## SQL 예시
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
