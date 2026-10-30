---
title: DEGREES (Lakehouse v1)
description: DEGREES — 라디안으로 지정한 인수 x를 도 단위로 변환하여 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

인수 `x`를 라디안에서 도(degree) 단위로 변환하여 반환합니다. 이때 `x`는 라디안으로 지정합니다.

## Analyze Syntax

```python
func.degrees( <x> )
```

## Analyze Examples

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## SQL Syntax

```sql
DEGREES( <x> )
```

## SQL Examples

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
