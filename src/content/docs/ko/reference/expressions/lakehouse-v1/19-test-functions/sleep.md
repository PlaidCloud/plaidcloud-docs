---
title: SLEEP (Lakehouse v1)
description: SLEEP — 각 데이터 블록에서 지정한 초 동안 대기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

각 데이터 블록에서 `seconds`초 동안 대기합니다.

!!! warning 
    대기가 필요한 테스트에서만 사용합니다.


## SQL 구문

```sql
SLEEP(seconds)
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| seconds  | 0 이상의 숫자 또는 부동 소수점 수로 이루어진 상수 열이어야 합니다.｜

## 반환 유형

UInt8

## SQL 예제

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
