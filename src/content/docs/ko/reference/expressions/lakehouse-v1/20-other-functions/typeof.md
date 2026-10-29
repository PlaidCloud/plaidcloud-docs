---
title: TYPEOF (Lakehouse v1)
description: TYPEOF — TYPEOF 함수는 데이터 유형의 이름을 반환하는 데 사용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

TYPEOF 함수는 데이터 유형의 이름을 반환하는 데 사용합니다.

## Analyze 구문

```python
func.typeof( <expr> )
```

## Analyze 예제

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## SQL 구문

```sql
TYPEOF( <expr> )
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| `<expr>` | 임의의 식입니다. <br /> 열 이름, 다른 함수의 결과 또는 수학 연산일 수 있습니다.

## 반환 유형

문자열

## SQL 예제

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
